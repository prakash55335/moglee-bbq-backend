import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "YourPermanentCloudPassword123"  # Change this to your desired password!

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email='', password=password)
    print("🚀 Superuser created successfully inside cloud container!")
else:
    print("✅ Admin account is already configured.")
