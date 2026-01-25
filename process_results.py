#!/usr/bin/env python3
"""Download batch results and save summaries to data/summaries/."""

import os
import glob
import json
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.environ['DOUBLEWORD_AUTH_TOKEN'],
    base_url=os.environ['DOUBLEWORD_BASE_URL']
)

# Find most recent batch_id file
batch_id_files = glob.glob('batch_id_*.txt')
if not batch_id_files:
    print("Error: No batch_id_*.txt files found. Run submit_batch.py first.")
    exit(1)

latest_batch_id_file = max(batch_id_files, key=os.path.getmtime)
with open(latest_batch_id_file, 'r') as f:
    batch_id = f.read().strip()

print(f"Retrieving batch results: {batch_id}\n")

# Get batch status
batch = client.batches.retrieve(batch_id)

if batch.status != 'completed':
    print(f"✗ Batch not completed yet. Status: {batch.status}")
    exit(1)

print(f"✓ Batch completed successfully")
print(f"Output file ID: {batch.output_file_id}\n")

# Download results file
print("Downloading results...")
file_response = client.files.content(batch.output_file_id)

# Create summaries directory
summaries_dir = Path('data/summaries')
summaries_dir.mkdir(parents=True, exist_ok=True)
print(f"Summaries will be saved to: {summaries_dir}/\n")

# Process each result
results_count = 0
for line in file_response.text.split('\n'):
    if not line.strip():
        continue

    result = json.loads(line)
    custom_id = result['custom_id']

    # Extract summary from response
    summary = result['response']['body']['choices'][0]['message']['content']

    # Extract filename from custom_id (e.g., "summary-DGM" -> "DGM")
    filename = custom_id.replace('summary-', '')

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save summary with timestamp as markdown
    output_path = summaries_dir / f'{filename}_summary_{timestamp}.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"✓ Saved: {output_path}")
    results_count += 1

print(f"\n✓ Successfully processed {results_count} summaries")
