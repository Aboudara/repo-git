import inspect
import logging

def custum_Logger(self, logLevel=logging.DEBUG):
    #
    logger_name = inspect.stack()[1][3]
    #
    logger = logging.getLogger(logger_name)
    logger.setLevel(logLevel)
    #
    fh = logging.FileHandler("automation.log")
    #
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
    #
    fh.setFormatter(formatter)
    #
    logger.addHandler(fh)
    return logger


log = custum_Logger(Warning)
