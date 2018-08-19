"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

#asctime adds date/time to the log
#datefmt lets us specify how we want the date formatted
#%I is for 12 hour clock, %H would be for 24 hour clock
#%p is AM/PM
# : is the actual : char that appears in the log messages
# s is for space
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")