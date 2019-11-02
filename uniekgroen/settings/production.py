from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


#
# GENERAL SETTINGS
#

WSGI_APPLICATION = 'uniekgroen.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.uniekgroen.be', '.aws.amazon.com', '.herokuapp.com']

# Enforce SSL
SECURE_SSL_REDIRECT = True

#
# WHITENOISE CONFIG
#

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#
# DATABASE
#

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# AMAZON AWZS

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = 'uniekgroen'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.eu-central-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
