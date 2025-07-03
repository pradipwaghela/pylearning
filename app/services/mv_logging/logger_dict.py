import os 
import logging.config
import logging.handlers
import logging
from flask  import current_app

combine_file_path = os.path.join(os.environ.get('LOG_FILES_PATH'),"combine.log")
error_file_path = os.path.join(os.environ.get('LOG_FILES_PATH'),"error.log")

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
        },
        'simple': {
            'format': '%(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
        },
        'file_combine': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': combine_file_path,
            'formatter': 'detailed',
            'when': 'midnight',
            'level': 'DEBUG',
        },
        'file_error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': error_file_path,
            'formatter': 'detailed',
            'when': 'midnight',
            'level': 'ERROR',
        }
    },
    'loggers': {
        'root': {  # root logger
            'handlers': ["file_combine","file_error","console"],
            'level': 'DEBUG',
        }
    },
}

def setup_logger():
    """
    Setup custom logger for application 
    You can edit LOGGING_CONFIG in the logger_dict.py directory
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    