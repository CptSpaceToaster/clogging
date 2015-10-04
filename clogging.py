#!/usr/bin/env python3.4
# System
import logging


# TODO: Get another color utility library
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


_levelToColor = {
    logging.CRITICAL: Colors.magenta,
    logging.ERROR: Colors.red,
    logging.WARNING: Colors.yellow,
    logging.INFO: Colors.blue,
    logging.DEBUG: Colors.cyan,
    logging.NOTSET: Colors.white,
}


class ClogRecord(logging.LogRecord):
    def __init__(self, name, level, pathname, lineno,
                 msg, args, exc_info, func=None, sinfo=None, **kwargs):
        super().__init__(name, level, pathname, lineno,
                         msg, args, exc_info, func=None, sinfo=None, **kwargs)
        self.reset = Colors.reset
        self.levelcolor = _levelToColor[level]

# Override the LogRecordFactory to use ours, which provides %(color)s and %(reset)s
logging.setLogRecordFactory(ClogRecord)


if __name__ == '__main__':
    logger = logging.getLogger()
    # This is needed to make the logger care about messages DEBUG and over
    logger.setLevel(logging.DEBUG)

    # An uncolored formatter
    logFormatter = logging.Formatter('[%(asctime)s] [ %(levelname)-8s ]: %(message)-1s')
    # A formatter that makes use of the new fields 'levelcolor' and 'reset'
    clogFormatter = logging.Formatter('[%(asctime)s] [ %(levelcolor)s%(levelname)-8s%(reset)s ]: %(message)-1s')

    fileHandler = logging.FileHandler('tst.log')
    # make it care about messages DEBUG and over
    fileHandler.setLevel(logging.DEBUG)
    # attach the uncolored formatter
    fileHandler.setFormatter(logFormatter)
    # smells like coffee in here
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    # make it care about messages DEBUG and over
    consoleHandler.setLevel(logging.DEBUG)
    # attach the COLORED formatter!
    consoleHandler.setFormatter(clogFormatter)
    # really smells like coffee.......
    logger.addHandler(consoleHandler)

    logger.debug('hello')
    logger.info('waffle')
    logger.warning('is')
    logger.error('a')
    logger.critical('message')
