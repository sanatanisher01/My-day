#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Running startup script ==="

# Set up the database
echo "=== Setting up database ==="
python setup_database.py

# Start the application
echo "=== Starting application ==="
exec "$@"
