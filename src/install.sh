#!/bin/sh

# Exit when any command fails
set -e

# Run Installation Script
python3 install.py

# Delete Installation Files
rm install.py
rm install.json
rm install.sh

exit 0
