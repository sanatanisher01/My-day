#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Running startup script ==="

# Set up the database
echo "=== Setting up database ==="
python initialize_database.py

# Fix content types specifically
echo "=== Fixing content types ==="
python fix_content_types.py

# Create a simple index.html file for testing
echo "=== Creating test page ==="
mkdir -p staticfiles
cat > staticfiles/index.html << EOL
<!DOCTYPE html>
<html>
<head>
    <title>MyDay - Test Page</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #4a6da7; }
        .container { max-width: 800px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>MyDay Test Page</h1>
        <p>If you can see this page, the server is running correctly.</p>
        <p>This is a temporary page to verify that the server is working.</p>
        <p>Try accessing the <a href="/events/">events page</a> or the <a href="/accounts/login/">login page</a>.</p>
    </div>
</body>
</html>
EOL

# Start the application
echo "=== Starting application ==="
exec "$@"
