from decouple import config

# Database settings
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASES
DATABASE_CONFIG = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('DATABASES_NAME'),
    }
}
