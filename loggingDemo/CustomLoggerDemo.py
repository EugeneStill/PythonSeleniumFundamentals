import logging
import loggingDemo.CustomLogger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    # If we create logging object at the class level then the log file will be named after the class.
    # For method1 we are using the logging object created at the class level.
    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    # If we create a logging object in a method (like in method2 & method3 then the log file is named after that method
    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warn('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):
        m3Log = cl.customLogger(logging.INFO)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warn('warn message')
        m3Log.error('error message')
        m3Log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()