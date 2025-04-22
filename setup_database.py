"""
Script to set up the database directly.
This will create all necessary tables and mark migrations as applied.
"""
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def setup_database():
    """Set up the database directly."""
    print("Setting up database directly...")
    
    try:
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
            
            # Check if django_migrations table exists
            cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'django_migrations'
            );
            """)
            table_exists = cursor.fetchone()[0]
            
            if table_exists:
                # Mark all migrations as applied
                cursor.execute("""
                INSERT INTO django_migrations (app, name, applied)
                VALUES 
                    ('chat', '0001_initial', NOW())
                ON CONFLICT DO NOTHING;
                """)
                print("Marked migrations as applied")
            else:
                print("django_migrations table doesn't exist yet")
        
        print("Database setup complete.")
        return True
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False

if __name__ == "__main__":
    success = setup_database()
    sys.exit(0 if success else 1)
