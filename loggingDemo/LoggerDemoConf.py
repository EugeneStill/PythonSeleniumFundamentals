"""
Logger Demo
"""
import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        # create logger using config file
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages written to the text file based on config
        logger.debug('debug 1 message')
        logger.info('info 0 message')
        logger.warn('warn 3 message')
        logger.error('error 4 message')
        logger.critical('critical ! message')

demo = LoggerDemoConf()
demo.testLog()