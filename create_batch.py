#!/usr/bin/env python3
"""Create JSONL batch requests with robust PDF extraction and fallback methods."""

import json
import os
from pathlib import Path
from pypdf import PdfReader
import pdfplumber
import glob
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Read summarization prompt and substitute word count
with open('summarisation_prompt_sample.txt', 'r') as f:
    prompt_template = f.read()

# Substitute word count from environment variable (default to 2000)
word_count = os.getenv('SUMMARY_WORD_COUNT', '2000')
prompt_template = prompt_template.replace('{WORD_COUNT}', word_count)

# Collect all PDF files from data/papers directory
pdf_files = glob.glob('data/papers/*.pdf')
pdf_files.sort()  # Sort for consistent ordering

print(f"Found {len(pdf_files)} PDF files to process\n")

requests = []
failed_files = []
extraction_stats = {'pypdf': 0, 'pdfplumber': 0}

def extract_text_pypdf(pdf_path):
    """Try pypdf first (faster)."""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        text = '\n'.join(page.extract_text() for page in reader.pages)
        return text, len(reader.pages)

def extract_text_pdfplumber(pdf_path):
    """Fallback to pdfplumber (more robust but slower)."""
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join((page.extract_text() or '') for page in pdf.pages)
        return text, len(pdf.pages)

for idx, pdf_path in enumerate(pdf_files, 1):
    print(f"[{idx}/{len(pdf_files)}] Processing {pdf_path}...")

    text = None
    pages = 0
    extraction_method = None

    try:
        # Try pypdf first (faster)
        text, pages = extract_text_pypdf(pdf_path)
        extraction_method = 'pypdf'
        extraction_stats['pypdf'] += 1

    except (KeyError, Exception) as e:
        if 'bbox' in str(e) or isinstance(e, KeyError):
            # Fallback to pdfplumber for bbox errors
            try:
                print(f"  ⚠ pypdf failed ({e}), trying pdfplumber...")
                text, pages = extract_text_pdfplumber(pdf_path)
                extraction_method = 'pdfplumber'
                extraction_stats['pdfplumber'] += 1
            except Exception as e2:
                print(f"  ✗ Both methods failed: {e2}")
                failed_files.append((pdf_path, f"pypdf: {e}, pdfplumber: {e2}"))
                continue
        else:
            print(f"  ✗ Error: {e}")
            failed_files.append((pdf_path, str(e)))
            continue

    # Skip if no meaningful text extracted
    if not text or len(text.strip()) < 100:
        print(f"  ⚠ Skipped (insufficient text: {len(text)} chars)")
        failed_files.append((pdf_path, "insufficient text"))
        continue

    print(f"  ✓ Extracted {len(text)} characters from {pages} pages [{extraction_method}]")

    # Create batch request with sanitized custom_id
    # Remove special chars from filename for custom_id (max 64 chars including 'summary-' prefix)
    safe_filename = Path(pdf_path).stem.replace('%', '_').replace(' ', '_').replace('&', 'and')[:55]

    request = {
        "custom_id": f"summary-{safe_filename}",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "Qwen/Qwen3-VL-235B-A22B-Instruct-FP8",
            "messages": [
                {
                    "role": "user",
                    "content": f"{prompt_template}\n\nDocument text:\n{text}"
                }
            ],
            "max_tokens": 5000  # Budget for reasoning tokens + 2000 word summary
        }
    }
    requests.append(request)

# Write JSONL file with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'batch_requests_{timestamp}.jsonl'
with open(output_file, 'w') as f:
    for req in requests:
        f.write(json.dumps(req) + '\n')

print(f"\n{'='*60}")
print(f"✓ Created {output_file} with {len(requests)} requests")
print(f"\nExtraction methods used:")
print(f"  pypdf: {extraction_stats['pypdf']} files")
print(f"  pdfplumber (fallback): {extraction_stats['pdfplumber']} files")

if failed_files:
    print(f"\n⚠ Failed to process {len(failed_files)} files:")
    for path, reason in failed_files:
        print(f"  - {Path(path).name}: {reason}")

print(f"\nNext step: python submit_batch.py")
