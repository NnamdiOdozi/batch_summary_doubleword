#!/usr/bin/env python3
"""
Orchestrator script for the batch summarization pipeline.
Runs all three stages: extraction, submission, and polling.

Usage:
  # Process all files in default directory (data/papers/)
  python run_batch_pipeline.py

  # Process specific files
  python run_batch_pipeline.py --files paper1.pdf paper2.txt report.docx

  # Process all files in a custom directory
  python run_batch_pipeline.py --input-dir /path/to/documents/
"""

import os
import sys
import argparse
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


def run_stage(stage_num, description, script_name, extra_args=None):
    """Run a pipeline stage."""
    print_header(f"STAGE {stage_num}: {description}")

    cmd = [sys.executable, script_name]
    if extra_args:
        cmd.extend(extra_args)

    try:
        result = subprocess.run(
            cmd,
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
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Run the complete batch summarization pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Process all files in default directory (data/papers/)
  python run_batch_pipeline.py

  # Process specific files
  python run_batch_pipeline.py --files paper1.pdf paper2.txt report.docx

  # Process all files in a custom directory
  python run_batch_pipeline.py --input-dir /path/to/documents/
'''
    )
    parser.add_argument(
        '--files',
        nargs='+',
        metavar='FILE',
        help='Specific file paths to process'
    )
    parser.add_argument(
        '--input-dir',
        metavar='DIR',
        help='Directory to scan for documents (default: data/papers/)'
    )

    args = parser.parse_args()

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

    # Prepare arguments for create_batch.py
    create_batch_args = []
    if args.files:
        create_batch_args.extend(['--files'] + args.files)
    elif args.input_dir:
        create_batch_args.extend(['--input-dir', args.input_dir])

    # Stage 1: Extract documents and create batch requests
    if not run_stage(
        1,
        "Extracting documents and creating batch requests",
        "create_batch.py",
        extra_args=create_batch_args if create_batch_args else None
    ):
        sys.exit(1)

    # Stage 2: Submit batch to Doubleword API
    if not run_stage(
        2,
        "Submitting batch to Doubleword API",
        "submit_batch.py"
    ):
        sys.exit(1)

    # Allow time for batch ID propagation before polling
    print("\nWaiting for batch ID to propagate...")
    import time
    time.sleep(10)  # Wait 10 seconds for the batch to be queryable

    # Stage 3: Poll and process results
    if not run_stage(
        3,
        "Polling for results and processing summaries",
        "poll_and_process.py"
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
