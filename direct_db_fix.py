"""
Direct SQL script to fix the database.
This script uses raw SQL to fix the database without relying on Django ORM.
"""
import os
import sys
import psycopg2
from urllib.parse import urlparse
import dj_database_url

def get_db_connection():
    """Get a connection to the database."""
    # Get the database URL from the environment
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("DATABASE_URL environment variable not set")
        return None
    
    # Parse the database URL
    config = dj_database_url.parse(database_url)
    
    # Connect to the database
    try:
        conn = psycopg2.connect(
            dbname=config['NAME'],
            user=config['USER'],
            password=config['PASSWORD'],
            host=config['HOST'],
            port=config['PORT']
        )
        conn.autocommit = True
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def fix_database():
    """Fix the database using direct SQL."""
    print("Starting direct database fix...")
    
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        with conn.cursor() as cursor:
            # Fix content types
            print("Fixing content types...")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS django_content_type (
                id serial PRIMARY KEY,
                app_label varchar(100) NOT NULL,
                model varchar(100) NOT NULL,
                name varchar(100) NOT NULL
            );
            """)
            
            # Update null names in content types
            cursor.execute("""
            UPDATE django_content_type 
            SET name = app_label || '_' || model 
            WHERE name IS NULL;
            """)
            
            # Create auth_user table if it doesn't exist
            print("Creating auth_user table if it doesn't exist...")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS auth_user (
                id serial PRIMARY KEY,
                password varchar(128) NOT NULL,
                last_login timestamp with time zone,
                is_superuser boolean NOT NULL,
                username varchar(150) NOT NULL UNIQUE,
                first_name varchar(150) NOT NULL,
                last_name varchar(150) NOT NULL,
                email varchar(254) NOT NULL,
                is_staff boolean NOT NULL,
                is_active boolean NOT NULL,
                date_joined timestamp with time zone NOT NULL
            );
            """)
            
            # Create chat_chatmessage table if it doesn't exist
            print("Creating chat_chatmessage table if it doesn't exist...")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_chatmessage (
                id serial PRIMARY KEY,
                message text NOT NULL,
                timestamp timestamp with time zone NOT NULL,
                is_read boolean NOT NULL,
                receiver_id integer NOT NULL,
                sender_id integer NOT NULL
            );
            """)
            
            # Create django_migrations table if it doesn't exist
            print("Creating django_migrations table if it doesn't exist...")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS django_migrations (
                id serial PRIMARY KEY,
                app varchar(255) NOT NULL,
                name varchar(255) NOT NULL,
                applied timestamp with time zone NOT NULL
            );
            """)
            
            # Mark chat migrations as applied
            print("Marking chat migrations as applied...")
            cursor.execute("""
            INSERT INTO django_migrations (app, name, applied)
            VALUES ('chat', '0001_initial', NOW())
            ON CONFLICT DO NOTHING;
            """)
            
            print("Database fix completed successfully")
        
        return True
    except Exception as e:
        print(f"Error fixing database: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    success = fix_database()
    sys.exit(0 if success else 1)
