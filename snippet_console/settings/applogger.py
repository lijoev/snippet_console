import os

from decouple import config

ROOT_DIR = config('ROOT_DIR', '')
LOGS_DIR = os.path.join(ROOT_DIR, 'logs')

LOGS_PREFIX = 'app.out.'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s %(name)s [%(pathname)s:"
                      "%(lineno)d] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'verbose': {'format': '{levelname} {message}','style': '{', },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_PREFIX + 'console.log'),
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 10,
            'formatter': 'standard',
        },
        'logfile_custom': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_PREFIX +
                                     'custom_debug.log'),
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 10,
            'formatter': 'standard',
        },
        'logfile_bardrequests': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_PREFIX +
                                     'badrequests.log'),
            'formatter': 'standard',
        },

        'logfile_api_views': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_PREFIX +
                                     'api-views.log'),
            'formatter': 'standard',
        },
        'db_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_PREFIX + 'db-queries.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['db_handler'],
            'level': 'INFO',  # no need to display the database query while
            # hitting the database
            'propagate': False,  # if need changed into True and DEBUG
        },
        'bad_requests': {
            'handlers': ['logfile_bardrequests'],
            'level': 'DEBUG',
        },
        'api_views': {
            'handlers': ['logfile_api_views'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'custom_logger': {
            'handlers': ['logfile_custom'],
            'level': 'INFO',
        },

    }
}
