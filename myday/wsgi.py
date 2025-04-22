"""
WSGI config for myday project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')

# Try to set up the database before starting the application
try:
    # Only run in production (Render)
    if os.environ.get('RENDER', '') == 'true':
        # Add the project root to the path
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from setup_database import setup_database
        setup_database()
except Exception as e:
    print(f"Error setting up database: {e}")

application = get_wsgi_application()
