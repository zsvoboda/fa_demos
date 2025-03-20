import logging
import sys
import os


def setup_logging():
    log_level = os.getenv('PS_LOG_LEVEL', 'INFO')
    logging.basicConfig(stream=sys.stdout, level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    setup_logging()
