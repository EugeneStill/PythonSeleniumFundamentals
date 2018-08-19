"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import logging

#WRITES TO FILE IN PACKAGE DIRECTORY
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
