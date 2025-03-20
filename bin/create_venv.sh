#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Create a virtual environment in the bin directory
python3 -m venv $THIS_DIR/../.venv

# Activate the virtual environment
source $THIS_DIR/.venv/bin/activate

echo "Virtual environment created and activated in $THIS_DIR/.venv"