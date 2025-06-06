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

        # First try to fix content types specifically
        try:
            from fix_content_types import fix_content_types
            fix_content_types()
        except ImportError:
            print("Content type fix script not found")
        except Exception as e:
            print(f"Error fixing content types: {e}")

        # Then run the full database initialization
        try:
            from initialize_database import initialize_database
            initialize_database()
        except ImportError:
            # Fall back to the old script if the new one is not available
            try:
                from fix_database import fix_database
                fix_database()
            except ImportError:
                print("No database initialization script found")
            except Exception as e:
                print(f"Error running fix_database: {e}")
        except Exception as e:
            print(f"Error running initialize_database: {e}")
except Exception as e:
    print(f"Error setting up database: {e}")

application = get_wsgi_application()
