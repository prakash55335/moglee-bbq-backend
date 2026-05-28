import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
password = "YourPermanentCloudPassword123"  # Set your desired admin password here

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email='', password=password)
    print("🚀 Cloud Admin created successfully with Custom User Model!")
else:
    print("✅ Admin account is already configured.")
