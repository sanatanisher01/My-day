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

# Run migrations with comprehensive error handling
echo "=== Running migrations ==="

# First try to run migrations normally
python manage.py migrate --noinput || {
    echo "=== Migration failed, trying alternative approach ==="

    # Try to fix the database directly
    echo "=== Attempting to fix database directly ==="
    python fix_render_db.py

    # Try to fix chat migrations specifically
    echo "=== Fixing chat migrations ==="
    # Rename the problematic migration file
    if [ -f "chat/migrations/0002_remove_chatmessage_image_remove_chatmessage_room_and_more.py" ]; then
        mv chat/migrations/0002_remove_chatmessage_image_remove_chatmessage_room_and_more.py chat/migrations/0002_remove_chatmessage_image_remove_chatmessage_room_and_more.py.bak
    fi

    # Use our fixed initial migration
    if [ -f "chat/migrations/0001_initial_fixed.py" ]; then
        cp chat/migrations/0001_initial_fixed.py chat/migrations/0001_initial.py
    fi

    # Create initial migrations for all apps
    echo "=== Creating initial migrations ==="
    python manage.py makemigrations accounts bookings events

    # Try to apply migrations with --fake-initial
    echo "=== Applying initial migrations with --fake-initial ==="
    python manage.py migrate --noinput --fake-initial

    # If that fails, try with --fake
    if [ $? -ne 0 ]; then
        echo "=== Applying migrations with --fake ==="
        python manage.py migrate --fake

        # If that still fails, try one more approach
        if [ $? -ne 0 ]; then
            echo "=== Final migration attempt ==="
            # Apply migrations one by one
            python manage.py migrate auth --fake
            python manage.py migrate contenttypes --fake
            python manage.py migrate sessions --fake
            python manage.py migrate admin --fake
            python manage.py migrate accounts --fake
            python manage.py migrate events --fake
            python manage.py migrate bookings --fake
            python manage.py migrate chat --fake
        fi
    fi
}

echo "=== Build process completed successfully ==="
