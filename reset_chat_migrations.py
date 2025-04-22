"""
Script to completely reset chat app migrations.
This will remove all existing migrations and create a fresh initial migration.
"""
import os
import sys
import shutil
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def reset_chat_migrations():
    """Reset chat app migrations."""
    print("Resetting chat app migrations...")
    
    # Path to chat migrations
    migrations_path = os.path.join('chat', 'migrations')
    
    # Create backup directory
    backup_path = os.path.join(migrations_path, 'backup')
    os.makedirs(backup_path, exist_ok=True)
    
    # Move all migration files except __init__.py to backup
    for filename in os.listdir(migrations_path):
        if filename.endswith('.py') and filename != '__init__.py':
            src = os.path.join(migrations_path, filename)
            dst = os.path.join(backup_path, filename)
            if os.path.exists(src):
                shutil.move(src, dst)
                print(f"Backed up {filename}")
    
    # Create a fresh initial migration
    print("Creating fresh initial migration...")
    with open(os.path.join(migrations_path, '0001_initial.py'), 'w') as f:
        f.write("""from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
""")
    
    print("Chat migrations reset complete.")

if __name__ == "__main__":
    reset_chat_migrations()
