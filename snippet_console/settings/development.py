from .base import *

DEBUG = True
ENVIRONMENT = 'development'
ADMIN_SITE_HEADER = 'SNIPPET CONSOLE - DEVELOPMENT'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = config('STATIC_URL', '/static/')
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, 'app_static'),
]

# Media Settings (media url, media root etc)
# https://docs.djangoproject.com/en/3.0/ref/settings/#media-root
MEDIA_URL = config('MEDIA_URL', '/media/')
MEDIA_DIR_NAME = 'media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, MEDIA_DIR_NAME)
# import application log settings
try:
    from .applogger import *
except ImportError:
    pass

