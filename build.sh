#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Starting build process ==="

# Install dependencies with pip cache
echo "=== Installing dependencies ==="
pip install --no-cache-dir -r requirements.txt

# Clean up pip cache to save memory
rm -rf ~/.cache/pip

# Collect static files
echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

# Run migrations with reduced memory usage
echo "=== Running migrations ==="
PYTHONUNBUFFERED=1 python -B manage.py migrate

# Create a superuser if needed (only in development)
if [ "$DJANGO_DEBUG" = "True" ]; then
  echo "=== Creating superuser ==="
  python manage.py createsuperuser --noinput || true
fi

echo "=== Build process completed successfully ==="
