import os
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

# Explicit database configuration completely bypassing external parser libraries
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.qkwvpflnrwtfufmlwpcx',
        'PASSWORD': 'Prakash5533*Moglee#DB',
        'HOST': '://supabase.com',
        'PORT': '6543',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
