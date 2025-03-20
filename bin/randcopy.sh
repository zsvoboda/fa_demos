#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PYTHONPATH=$THIS_DIR/../src

python3 $PYTHONPATH/util/randcopy.py $@