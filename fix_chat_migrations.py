"""
Script to fix chat app migrations.
This script will create a new initial migration for the chat app.
"""
import os
import sys
import shutil
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def fix_chat_migrations():
    """Fix chat app migrations."""
    print("Fixing chat app migrations...")
    
    # Path to chat migrations
    migrations_path = os.path.join('chat', 'migrations')
    
    # Backup existing migrations
    backup_path = os.path.join(migrations_path, 'backup')
    os.makedirs(backup_path, exist_ok=True)
    
    # Move existing migrations to backup
    for filename in os.listdir(migrations_path):
        if filename.endswith('.py') and filename != '__init__.py':
            src = os.path.join(migrations_path, filename)
            dst = os.path.join(backup_path, filename)
            shutil.move(src, dst)
            print(f"Backed up {filename}")
    
    # Create a new initial migration
    os.system('python manage.py makemigrations chat')
    
    print("Chat migrations fixed.")

if __name__ == "__main__":
    fix_chat_migrations()
