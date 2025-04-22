import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
User.objects.create_superuser(
    username='aryangupta@010',
    email='aryansanatani01@gmail.com',
    password='Akrat@010'
)

print("Superuser created successfully!") 