#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC_DIR=$THIS_DIR/../src
LIB_DIR=$THIS_DIR/../lib
ROOT_DIR=$THIS_DIR/..
export PYTHONPATH=$SRC_DIR:$ROOT_DIR:$LIB_DIR

python3 $SRC_DIR/util/randcopy.py $@