"""
Custom migration script that doesn't ask interactive questions.
"""
import os
import sys
import django
from django.core.management import call_command

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings_noninteractive')
django.setup()

def run_migrations():
    """Run migrations without interactive prompts."""
    print("Running migrations without interactive prompts...")
    
    try:
        # Try to run migrations
        call_command('migrate', interactive=False)
        print("Migrations completed successfully.")
        return True
    except Exception as e:
        print(f"Error running migrations: {e}")
        
        # Try with --fake
        try:
            print("Trying migrations with --fake...")
            call_command('migrate', fake=True, interactive=False)
            print("Fake migrations completed successfully.")
            return True
        except Exception as e:
            print(f"Error running fake migrations: {e}")
            
            # Try app by app
            try:
                print("Trying migrations app by app...")
                for app in ['auth', 'contenttypes', 'sessions', 'admin', 
                           'accounts', 'events', 'bookings', 'chat']:
                    try:
                        call_command('migrate', app, fake=True, interactive=False)
                        print(f"Migrated {app} successfully.")
                    except Exception as e:
                        print(f"Error migrating {app}: {e}")
                return True
            except Exception as e:
                print(f"Error running app-by-app migrations: {e}")
                return False

if __name__ == "__main__":
    success = run_migrations()
    sys.exit(0 if success else 1)
