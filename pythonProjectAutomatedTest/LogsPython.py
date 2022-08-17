import inspect
import logging

class custLogger:
    def custLogger(self, logLevel=logging.DEBUG):
        #
        logger_name = inspect.stack()[1][3]
        #
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        #
        fh = logging.FileHandler("automation.log")
        #
        formatter = logging.Formatter('%(asctime)s - %(levelname)s')


"""logging.basicConfig(level=logging.INFO, filename="mylog.txt", format='%(asctime)s %(message)s')

logging.info('test')
logging.info('test2')"""
