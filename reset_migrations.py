"""
Script to reset migrations for a fresh database.
This script will be used to create initial migrations for all apps.
"""
import os
import sys
import django
from django.db import connection
from django.apps import apps

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def reset_migrations():
    """Reset migrations for all apps."""
    print("Resetting migrations...")
    
    # Get all app configs
    app_configs = apps.get_app_configs()
    app_names = [app.label for app in app_configs if not app.name.startswith('django.')]
    
    print(f"Found apps: {', '.join(app_names)}")
    
    # Create initial migrations for each app
    for app_name in app_names:
        print(f"Creating initial migration for {app_name}...")
        os.system(f"python manage.py makemigrations {app_name}")
    
    print("Migrations reset complete.")

if __name__ == "__main__":
    reset_migrations()
