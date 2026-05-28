"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://djangoproject.com
"""

import os

from django.core.wsgi import get_wsgi_application

# Force Django to look into settings/production.py on your production server
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()
