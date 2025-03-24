#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Activate the virtual environment
source $THIS_DIR/../.venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install $THIS_DIR/../lib/pypureclient.tar.gz

echo "Virtual environment activated from source ($THIS_DIR/../.venv/bin/activate) and all required packages installed."