#!/bin/sh

# Exit when any command fails
set -e

# Delete older sources
./clean.sh

# Copy Sources files for test
cp -R src build

exit 0
