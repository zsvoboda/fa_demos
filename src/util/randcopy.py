import os
import sys

import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log import setup_logging
setup_logging()
_logger = logging.getLogger(__name__)

from env import load_env
load_env()


def randcopy(_size=1024*1024*1024, _out_file="output.bin"):
    with open(_out_file, "wb") as f:
        f.write(os.urandom(_size))      
    
if __name__ == '__main__':
    # Take the first commandline parameter as the name of the file to be generated
    # Take the -n parameter as the size of the file to be generated
    import sys
    import getopt
    
    _size = 1024*1024*1024
    _out_file = "output.bin"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:")
        for opt, arg in opts:
            if opt == "-n":
                _size = int(arg)
            else:
                _logger.error("Unknown option: " + opt)
                sys.exit(2)
        if len(args) > 0:
            _out_file = args[0]
    except getopt.GetoptError as err:
        _logger.error(str(err))
        _logger.info("Usage: randcopy [-n size] [outputfile]")
        sys.exit(2)
    _logger.info(f"Generating file {_out_file} of size {_size}.")
    
    randcopy(_size, _out_file)