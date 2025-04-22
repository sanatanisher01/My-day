"""
Script to fix database issues on Render.
This script will create tables directly if migrations fail.
"""
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def fix_database():
    """Fix database issues by creating tables directly."""
    print("Fixing database issues...")
    
    # Create chat_chatmessage table if it doesn't exist
    with connection.cursor() as cursor:
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
        print("Created chat_chatmessage table if it didn't exist")
    
    print("Database fix complete.")

if __name__ == "__main__":
    fix_database()
