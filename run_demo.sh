#!/bin/bash
set -e
set -x

echo "Starting Simple Blockchain demo..."

# Ensure output folders exist
mkdir -p charts outputs

# Run the root-level Python demo
python src/demo_blockchain.py

echo "Demo finished successfully."

