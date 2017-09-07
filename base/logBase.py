# coding; utf-8
import logging

from util.yamlUtil import *

from constant.constant import *


class BaseLog(object):
    def __init__(self):

        config_file = load_yaml(CONFIG_FILE_PATH)
        FORMAT = config_file['log']['fommat']
        DATEFMT = config_file['log']['datefmt']
        FILENAME = config_file['log']['file']['path']

        # file
        filehandler = logging.FileHandler(filename=FILENAME, encoding="utf-8")
        filehandler.setLevel(self.__set_level(config_file['log']['file']['level']))
        fmter = logging.Formatter(fmt=FORMAT, datefmt=DATEFMT)
        filehandler.setFormatter(fmter)

        # console
        console = logging.StreamHandler()
        console.setLevel(self.__set_level(config_file['log']['console']['level']))
        formatter = logging.Formatter(FORMAT)
        console.setFormatter(formatter)

        logging.basicConfig(level=logging.DEBUG, handlers=[console, filehandler])

        self.log = logging.getLogger("BaseLog")  # type: logging

    def __set_level(self, config):
        if config == 'DEBUG':
            return logging.DEBUG
        elif config == 'INFO':
            return logging.INFO
        elif config == 'WARNING':
            return logging.WARNING
        elif config == 'ERROR':
            return logging.ERROR

    # def getLogger(self, module):
    #     self.log = logging.getLogger(module)
    #     return self.log


if __name__ == '__main__':
    log = BaseLog().log
    log.debug("this is debug msg")
    log.info("this is info msg")
    log.warning("this is warning msg")
    log.error("this is error msg")

    log.info("this is a format: %s %s", "hello", "world")

    log = BaseLog().log
    log.info("this is info msg 爱爱爱")
