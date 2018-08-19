import inspect
import logging

def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    # Anile didn't explain what [1][3] are but this is how we get the name of class / method from the stack
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Use fileHandler to write logs to file. Set file name using loggerName
    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    # Add formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(fileHandler)

    return logger
