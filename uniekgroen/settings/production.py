from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


#
# GENERAL SETTINGS
#

WSGI_APPLICATION = 'healthhouse.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.uniekgroen.be', '.aws.amazon.com', '.herokuapp.com']

# Enforce SSL
SECURE_SSL_REDIRECT = True

#
# MIDDLEWARE
#

MIDDLEWARE += [
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
]

#
# DATABASE
#

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#
# STATIC FILES
#

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'