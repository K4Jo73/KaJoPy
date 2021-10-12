import logging
import os
import sys
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir):
    log_file_format = "[%(levelname)s] %(name)s - %(asctime)-15s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d"
    log_console_format = "[%(levelname)s] %(name)s: %(message)s"

    # Main logger
    main_logger = logging.getLogger()
    main_logger.setLevel(logging.ERROR) # Stop default console output
    # main_logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CRITICAL)
    console_handler.setFormatter(logging.Formatter(log_console_format))

    exp_file_handler = RotatingFileHandler('{}exp_debug.log'.format(log_dir), maxBytes=10**6, backupCount=5)
    exp_file_handler.setLevel(logging.INFO)
    exp_file_handler.setFormatter(logging.Formatter(log_file_format))

    exp_errors_file_handler = RotatingFileHandler('{}exp_error.log'.format(log_dir), maxBytes=10**6, backupCount=5)
    exp_errors_file_handler.setLevel(logging.WARNING)
    exp_errors_file_handler.setFormatter(logging.Formatter(log_file_format))

    # main_logger.addHandler(console_handler)
    main_logger.addHandler(exp_file_handler)
    main_logger.addHandler(exp_errors_file_handler) 

