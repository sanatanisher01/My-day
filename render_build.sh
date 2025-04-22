#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Starting Render build process ==="

# Install dependencies with pip cache
echo "=== Installing dependencies ==="
pip install --no-cache-dir -r requirements.txt

# Clean up pip cache to save memory
rm -rf ~/.cache/pip

# Collect static files
echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

# Set environment variable to avoid interactive prompts
export DJANGO_SETTINGS_MODULE=myday.settings
export PYTHONPATH=$PYTHONPATH:$(pwd)
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_USERNAME=admin

# Run migrations with non-interactive approach
echo "=== Running migrations ==="

# First try to fix the database directly
echo "=== Attempting to fix database directly ==="
python fix_render_db.py

# Create a special settings file for non-interactive migrations
cat > non_interactive_settings.py << EOL
# Non-interactive settings for migrations
from myday.settings import *

DJANGO_MIGRATIONS_DISABLE_INTERACTIVE = True
EOL

# Make sure the merge migration exists
echo "=== Ensuring merge migration exists ==="
if [ ! -f "chat/migrations/0003_merge.py" ]; then
    echo "Creating merge migration for chat app"
    cat > chat/migrations/0003_merge.py << EOL
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0001_initial'),
        ('chat', '0002_remove_chatmessage_image_remove_chatmessage_room_and_more'),
    ]

    operations = [
        # No operations needed, this just merges the migrations
    ]
EOL
fi

# Run our custom migration script
echo "=== Running custom migration script ==="
python custom_migrate.py

# If that fails, try a more direct approach
if [ $? -ne 0 ]; then
    echo "=== Custom migration failed, trying direct SQL approach ==="

    # Create tables directly using SQL
    echo "=== Creating tables directly with SQL ==="
    python << EOL
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

with connection.cursor() as cursor:
    # Create chat_chatmessage table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_chatmessage (
        id bigserial PRIMARY KEY,
        message text NOT NULL,
        timestamp timestamp with time zone NOT NULL,
        is_read boolean NOT NULL,
        receiver_id integer NOT NULL REFERENCES auth_user(id),
        sender_id integer NOT NULL REFERENCES auth_user(id)
    );
    """)
    print("Created chat_chatmessage table")

    # Mark migrations as applied
    cursor.execute("""
    INSERT INTO django_migrations (app, name, applied)
    VALUES
        ('chat', '0001_initial', NOW()),
        ('chat', '0002_remove_chatmessage_image_remove_chatmessage_room_and_more', NOW()),
        ('chat', '0003_merge', NOW())
    ON CONFLICT DO NOTHING;
    """)
    print("Marked migrations as applied")
EOL
fi

echo "=== Build process completed successfully ==="
