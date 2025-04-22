#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Starting build process ==="

# Install dependencies
echo "=== Installing dependencies ==="
pip install -r requirements.txt

# Collect static files
echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

# Run migrations
echo "=== Running migrations ==="
python manage.py migrate

echo "=== Build process completed successfully ==="
