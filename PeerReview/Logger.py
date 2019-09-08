"""Logger: Settings for logfile creations"""
import logging
import logging.config

dictLogConfig = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'app.log',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}


def getLogger(app_name):
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger(app_name)
    return logger
