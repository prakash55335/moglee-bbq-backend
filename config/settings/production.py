import os
import dj_database_url
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

# Hardcoding your correct encoded Supabase pooler link directly so it never fails
DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://postgres.qkwvpflnrwtfufmlwpcx:Prakash5533%2AMoglee%23DB@://supabase.com'
    )
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
