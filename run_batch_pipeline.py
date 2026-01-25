#!/usr/bin/env python3
"""
Orchestrator script for the batch summarization pipeline.
Runs all three stages: extraction, submission, and polling.
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv


def print_header(text):
    """Print a formatted section header."""
    print("\n" + "=" * 50)
    print(text)
    print("=" * 50)


def validate_environment():
    """Validate that all required environment variables are set."""
    required_vars = [
        'DOUBLEWORD_AUTH_TOKEN',
        'DOUBLEWORD_BASE_URL',
        'DOUBLEWORD_MODEL'
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print("Error: Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease check your .env file")
        sys.exit(1)

    print("✓ Environment variables loaded")
    print(f"  Base URL: {os.getenv('DOUBLEWORD_BASE_URL')}")
    print(f"  Model: {os.getenv('DOUBLEWORD_MODEL')}")
    print(f"  Polling interval: {os.getenv('POLLING_INTERVAL', '30')} seconds")


def run_stage(stage_num, description, script_name):
    """Run a pipeline stage."""
    print_header(f"STAGE {stage_num}: {description}")

    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=True,
            capture_output=False
        )
        print(f"\n✓ Stage {stage_num} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error in stage {stage_num}")
        print(f"Script '{script_name}' failed with exit code {e.returncode}")
        return False


def main():
    """Run the complete batch processing pipeline."""
    print_header("Doubleword Batch Summarization Pipeline")

    # Check for .env file
    env_file = Path('.env')
    if not env_file.exists():
        print("\nError: .env file not found!")
        print("Please copy .env.sample to .env and fill in your credentials")
        sys.exit(1)

    # Load environment variables
    print("\nLoading environment variables from .env...")
    load_dotenv()

    # Validate environment
    validate_environment()

    # Stage 1: Extract PDFs and create batch requests
    if not run_stage(
        1,
        "Extracting PDFs and creating batch requests",
        "create_batch_requests_robust.py"
    ):
        sys.exit(1)

    # Stage 2: Submit batch to Doubleword API
    if not run_stage(
        2,
        "Submitting batch to Doubleword API",
        "submit_batch.py"
    ):
        sys.exit(1)

    # Stage 3: Poll and download results
    if not run_stage(
        3,
        "Polling for results and downloading",
        "poll_and_download.py"
    ):
        sys.exit(1)

    # Success!
    print_header("✓ Pipeline completed successfully!")
    print("\nSummaries saved to: data/summaries/")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
