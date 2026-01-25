#!/usr/bin/env python3
"""Poll batch job status and automatically download results when complete."""

import os
import glob
import time
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.environ['DOUBLEWORD_AUTH_TOKEN'],
    base_url=os.environ['DOUBLEWORD_BASE_URL']
)

# Get polling interval from environment variable (default: 30 seconds)
POLLING_INTERVAL = int(os.environ.get('POLLING_INTERVAL', '30'))

# Find most recent batch_id file
batch_id_files = glob.glob('batch_id_*.txt')
if not batch_id_files:
    print("Error: No batch_id_*.txt files found. Run submit_batch.py first.")
    exit(1)

latest_batch_id_file = max(batch_id_files, key=os.path.getmtime)
with open(latest_batch_id_file, 'r') as f:
    batch_id = f.read().strip()

print(f"Using batch ID from: {latest_batch_id_file}")

print(f"Polling batch job: {batch_id}")
print("Press Ctrl+C to stop polling\n")

try:
    while True:
        batch = client.batches.retrieve(batch_id)
        status = batch.status
        completed = batch.request_counts.completed
        total = batch.request_counts.total

        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Status: {status} | Progress: {completed}/{total}")

        if status == 'completed':
            print("\n✓ Batch completed successfully!")
            print("Downloading and processing results...\n")

            # Run process_results.py
            result = subprocess.run(['.venv/bin/python', 'process_results.py'])

            if result.returncode == 0:
                print("\n✓ All summaries saved to data/summaries/")
            else:
                print("\n✗ Error processing results")
            break

        elif status == 'failed':
            print(f"\n✗ Batch failed!")
            if hasattr(batch, 'errors') and batch.errors:
                print(f"Errors: {batch.errors}")
            break

        elif status == 'expired':
            print(f"\n✗ Batch expired!")
            break

        elif status == 'cancelled':
            print(f"\n✗ Batch was cancelled!")
            break

        # Wait before next check
        time.sleep(POLLING_INTERVAL)

except KeyboardInterrupt:
    print("\n\nPolling stopped by user")
    print(f"Current status: {status}")
    print("Run this script again to resume polling")
