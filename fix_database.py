"""
Legacy script for fixing database issues.
This script is kept for backward compatibility.
"""
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def fix_database():
    """Fix database issues."""
    print("Running legacy database fix...")
    
    try:
        with connection.cursor() as cursor:
            # Create chat_chatmessage table if it doesn't exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_chatmessage (
                id bigserial PRIMARY KEY,
                message text NOT NULL,
                timestamp timestamp with time zone NOT NULL,
                is_read boolean NOT NULL,
                receiver_id integer NOT NULL,
                sender_id integer NOT NULL
            );
            """)
            print("Created chat_chatmessage table if it didn't exist")
            
            # Fix content types
            cursor.execute("""
            UPDATE django_content_type 
            SET name = app_label || '_' || model 
            WHERE name IS NULL;
            """)
            print("Fixed null names in content types")
        
        return True
    except Exception as e:
        print(f"Error fixing database: {e}")
        return False

if __name__ == "__main__":
    success = fix_database()
    sys.exit(0 if success else 1)
