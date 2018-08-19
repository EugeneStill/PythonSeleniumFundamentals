"""
Logger Demo
"""
import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger log record object from the message string
        logger = logging.getLogger(LoggerDemoConsole.__name__) # use init to get set file name based on class
        #could use file name instead. file name appears in the console does not create a new file
        #logger = logging.getLogger('sample.log') # create logging object with file name
        logger.setLevel(logging.INFO)

        # create console handler object and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(consoleHandler)

        # use logger for logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()