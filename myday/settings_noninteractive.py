"""
Non-interactive settings for Django migrations.
This settings module is used during the build process to avoid interactive prompts.
"""
from .settings import *

# Import the custom questioner
from non_interactive_questioner import questioner

# Set the migration questioner to our non-interactive version
MIGRATION_MODULES = {
    'auth': 'django.contrib.auth.migrations',
    'contenttypes': 'django.contrib.contenttypes.migrations',
    'sessions': 'django.contrib.sessions.migrations',
    'admin': 'django.contrib.admin.migrations',
    'accounts': 'accounts.migrations',
    'events': 'events.migrations',
    'bookings': 'bookings.migrations',
    'chat': 'chat.migrations',
}

# This is a custom setting that will be checked in a custom migration command
DJANGO_MIGRATIONS_DISABLE_INTERACTIVE = True
