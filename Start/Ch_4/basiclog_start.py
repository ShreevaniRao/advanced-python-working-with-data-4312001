# demonstrate the logging api in Python
# use the built-in logging module
import logging

logging.basicConfig(level=logging.DEBUG,
                    filemode="w",
                    filename="output.log")

# Try out each of the log levels
logging.debug("This is a debug-level log message")
logging.info("This is an info-level log message")
logging.warning("This is a warning-level message")
logging.error("This is an error-level message")
logging.critical("This is a critical-level message")

# Output formatted string to the log
logging.info("Here's a {} variable and an int: {}".format("string", 10))


