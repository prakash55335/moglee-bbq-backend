# from config.settings.base import *
# from decouple import config

# DEBUG = False

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

# CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://localhost:5173').split(',')
# CORS_ALLOW_CREDENTIALS = True

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = False

from config.settings.base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = [
    '.railway.app',
    '.vercel.app',
    'localhost',
    '127.0.0.1',
    '*',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'