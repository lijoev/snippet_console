from .base import *

DEBUG = False
ENVIRONMENT = 'production'
ADMIN_SITE_HEADER = 'SNIPPET CONSOLE'

# import application log settings
try:
    from .applogger import *
except ImportError:
    pass

