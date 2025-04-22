"""
Script to fix the chat migrations.
This script removes conflicting migrations and creates a fresh initial migration.
"""
import os
import sys
import shutil
import django

# Set up Django first, before importing any models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def fix_chat_migrations():
    """Fix chat migrations by removing conflicting files and creating a fresh initial migration."""
    print("Fixing chat migrations...")
    
    try:
        # Path to the chat migrations directory
        migrations_dir = os.path.join('chat', 'migrations')
        
        # Create backup directory if it doesn't exist
        backup_dir = os.path.join(migrations_dir, 'backup')
        os.makedirs(backup_dir, exist_ok=True)
        
        # Backup and remove all existing migration files except __init__.py
        migration_files = []
        for filename in os.listdir(migrations_dir):
            filepath = os.path.join(migrations_dir, filename)
            if os.path.isfile(filepath) and filename != '__init__.py' and filename.endswith('.py'):
                # Backup the file
                backup_path = os.path.join(backup_dir, filename)
                try:
                    shutil.copy2(filepath, backup_path)
                    print(f"Backed up {filename}")
                    
                    # Remove the original file
                    os.remove(filepath)
                    print(f"Removed {filename}")
                    
                    migration_files.append(filename)
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
        
        # Create a fresh initial migration
        if migration_files:
            # Create a simple initial migration
            initial_migration_path = os.path.join(migrations_dir, '0001_initial.py')
            with open(initial_migration_path, 'w') as f:
                f.write("""from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='auth.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='auth.user')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
    ]
""")
            print("Created fresh initial migration")
        
        print("Chat migrations fixed successfully")
        return True
    except Exception as e:
        print(f"Error fixing chat migrations: {e}")
        return False

if __name__ == "__main__":
    success = fix_chat_migrations()
    sys.exit(0 if success else 1)
