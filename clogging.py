#!/usr/bin/env python3.4
# System
import logging


class Colors():
    # All colors are subject to change via terminal color schemes
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    light_gray = '\033[97m'
    dark_gray = '\033[90m'
    light_red = '\033[91m'
    light_green = '\033[92m'
    light_yellow = '\033[93m'
    light_blue = '\033[94m'
    light_magenta = '\033[95m'
    light_cyan = '\033[96m'
    white = '\033[97m'

    reset = '\033[0m'


def tint(msg, color):
    return color + msg + Colors.reset


class Colored_Handler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super().__init__(level=level)

    # TODO: Make a custom formatter/handler, that adds color
    def format(self, record):
        """
        Format the specified record.

        If a formatter is set, use it. Otherwise, use the default formatter
        for the module.
        """
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = logging._defaultFormatter
        return fmt.format(record)


if __name__ == '__main__':
    # This works, but it too much of a hack to be really useful.
    """
    logging._levelToName = {
        logging.CRITICAL: Colors.magenta + 'CRITICAL' + Colors.reset,
        logging.ERROR: Colors.red + 'ERROR' + Colors.reset,
        logging.WARNING: Colors.yellow + 'WARNING' + Colors.reset,
        logging.INFO: Colors.blue + 'INFO' + Colors.reset,
        logging.DEBUG: Colors.cyan + 'DEBUG' + Colors.reset,
        logging.NOTSET: Colors.white + 'NOTSET' + Colors.reset,
    }
    """

    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [ %(levelname)-17s ]: %(message)-1s')  # 8s -> 17s
    logger = logging.getLogger(__name__)

    logger.debug('hello')
    logger.info('waffle')
    logger.warning('is')
    logger.error('a')
    logger.critical('message')
