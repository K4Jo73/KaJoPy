import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Logging levels received
# info
# debug
# warning
# error
# critical



class CustomFileFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    info_format = "%(asctime)-15s %(message)s"
    debug_format = "%(asctime)-15s [%(levelname)s] \t : %(message)s"
    warning_format = "%(asctime)-15s [%(levelname)s] \t : %(message)s"
    error_format = "%(asctime)-15s [%(levelname)s] \t%(name)s : %(message)s \tin %(pathname)s:%(lineno)d"
    critical_format = "%(asctime)-15s [%(levelname)s] \t%(name)s : %(message)s \tin %(pathname)s:%(lineno)d"

    FORMATS = {
        logging.DEBUG: debug_format,
        logging.INFO: info_format,
        logging.WARNING: warning_format,
        logging.ERROR: error_format,
        logging.CRITICAL: critical_format
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)



class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    info_format = "%(message)s"
    debug_format = "[%(levelname)s] : %(message)s"
    warning_format = "[%(levelname)s] \t%(name)s : %(message)s"
    error_format = "[%(levelname)s] \t%(name)s : %(message)s \tin %(pathname)s:%(lineno)d"
    critical_format = "[%(levelname)s] \t%(name)s : %(message)s \tin %(pathname)s:%(lineno)d"

    FORMATS = {
        logging.DEBUG: grey + debug_format + reset,
        logging.INFO: grey + info_format + reset,
        logging.WARNING: yellow + warning_format + reset,
        logging.ERROR: red + error_format + reset,
        logging.CRITICAL: bold_red + critical_format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logging(log_dir):

    # Main logger
    main_logger = logging.getLogger()
    main_logger.setLevel(logging.DEBUG) # Stop default console output

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(CustomFormatter())

    exp_debug_file_handler = RotatingFileHandler('{}exp_debug.log'.format(log_dir), maxBytes=10**6, backupCount=5)
    exp_debug_file_handler.setLevel(logging.DEBUG)
    exp_debug_file_handler.setFormatter(CustomFileFormatter())

    exp_errors_file_handler = RotatingFileHandler('{}exp_error.log'.format(log_dir), maxBytes=10**6, backupCount=5)
    exp_errors_file_handler.setLevel(logging.ERROR)
    exp_errors_file_handler.setFormatter(CustomFileFormatter())

    main_logger.addHandler(console_handler)
    main_logger.addHandler(exp_debug_file_handler)
    main_logger.addHandler(exp_errors_file_handler) 

  