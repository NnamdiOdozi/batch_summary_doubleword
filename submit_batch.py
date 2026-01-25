#!/usr/bin/env python3
"""Upload batch requests and submit batch job to Doubleword API."""

import os
import glob
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with Doubleword credentials
client = OpenAI(
    api_key=os.environ['DOUBLEWORD_AUTH_TOKEN'],
    base_url=os.environ['DOUBLEWORD_BASE_URL']
)

# Find most recent batch_requests file
batch_files = glob.glob('batch_requests_*.jsonl')
if not batch_files:
    print("Error: No batch_requests_*.jsonl files found. Run create_batch.py first.")
    exit(1)

latest_batch_file = max(batch_files, key=os.path.getmtime)
print(f"Uploading {latest_batch_file}...")

# Upload batch file
with open(latest_batch_file, "rb") as file:
    batch_file = client.files.create(
        file=file,
        purpose="batch"
    )

print(f"File uploaded successfully!")
print(f"File ID: {batch_file.id}")

# Create batch job
completion_window = os.getenv('COMPLETION_WINDOW', '1h')
print(f"\nCreating batch job (completion window: {completion_window})...")
batch = client.batches.create(
    input_file_id=batch_file.id,
    endpoint=os.getenv('CHAT_COMPLETIONS_ENDPOINT', '/v1/chat/completions'),
    completion_window=completion_window
)

print(f"Batch job created successfully!")
print(f"Batch ID: {batch.id}")
print(f"Status: {batch.status}")

# Save batch ID for later retrieval with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
batch_id_file = f'batch_id_{timestamp}.txt'
with open(batch_id_file, 'w') as f:
    f.write(batch.id)

print(f"\nBatch ID saved to {batch_id_file}")
print("Next step: Run poll_and_process.py to monitor progress")
