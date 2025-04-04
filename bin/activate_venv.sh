#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Activate the virtual environment
source $THIS_DIR/../.venv/bin/activate

echo "Virtual environment activated from $THIS_DIR/../.venv"