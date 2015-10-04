#!/usr/bin/env python3.4
# System
import logging
import sys


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

logging.setLogRecordFactory(ClogRecord)


if __name__ == '__main__':
    logFormatter = logging.Formatter('[%(asctime)s] [ %(levelname)-8s ]: %(message)-1s')
    clogFormatter = logging.Formatter('[%(asctime)s] [ %(levelcolor)s%(levelname)-8s%(reset)s ]: %(message)-1s')
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('tst.log')
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(clogFormatter)
    logger.addHandler(consoleHandler)

    logger.debug('hello')
    logger.info('waffle')
    logger.warning('is')
    logger.error('a')
    logger.critical('message')