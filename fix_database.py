"""
Comprehensive script to fix database issues.
This script will fix content types and other database issues.
"""
import os
import sys
import django
from django.db import connection, transaction
from django.contrib.contenttypes.models import ContentType

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def fix_database():
    """Fix database issues comprehensively."""
    print("Starting comprehensive database fix...")
    
    try:
        # Fix content types
        fix_content_types()
        
        # Create necessary tables
        create_tables()
        
        # Mark migrations as applied
        mark_migrations_as_applied()
        
        print("Database fix completed successfully.")
        return True
    except Exception as e:
        print(f"Error fixing database: {e}")
        return False

def fix_content_types():
    """Fix content types with null names."""
    print("Fixing content types...")
    
    try:
        with connection.cursor() as cursor:
            # Check if django_content_type table exists
            cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'django_content_type'
            );
            """)
            table_exists = cursor.fetchone()[0]
            
            if table_exists:
                # Fix null names in content types
                cursor.execute("""
                UPDATE django_content_type 
                SET name = app_label || '_' || model 
                WHERE name IS NULL;
                """)
                print("Fixed null names in content types")
                
                # Ensure all models have content types
                with transaction.atomic():
                    for ct in ContentType.objects.all():
                        if not ct.name:
                            ct.name = f"{ct.app_label}_{ct.model}"
                            ct.save()
                    print("Updated content type names")
            else:
                print("django_content_type table doesn't exist yet")
    except Exception as e:
        print(f"Error fixing content types: {e}")
        raise

def create_tables():
    """Create necessary tables."""
    print("Creating necessary tables...")
    
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
    except Exception as e:
        print(f"Error creating tables: {e}")
        raise

def mark_migrations_as_applied():
    """Mark migrations as applied."""
    print("Marking migrations as applied...")
    
    try:
        with connection.cursor() as cursor:
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
                    ('contenttypes', '0001_initial', NOW()),
                    ('auth', '0001_initial', NOW()),
                    ('admin', '0001_initial', NOW()),
                    ('admin', '0002_logentry_remove_auto_add', NOW()),
                    ('admin', '0003_logentry_add_action_flag_choices', NOW()),
                    ('contenttypes', '0002_remove_content_type_name', NOW()),
                    ('auth', '0002_alter_permission_name_max_length', NOW()),
                    ('auth', '0003_alter_user_email_max_length', NOW()),
                    ('auth', '0004_alter_user_username_opts', NOW()),
                    ('auth', '0005_alter_user_last_login_null', NOW()),
                    ('auth', '0006_require_contenttypes_0002', NOW()),
                    ('auth', '0007_alter_validators_add_error_messages', NOW()),
                    ('auth', '0008_alter_user_username_max_length', NOW()),
                    ('auth', '0009_alter_user_last_name_max_length', NOW()),
                    ('auth', '0010_alter_group_name_max_length', NOW()),
                    ('auth', '0011_update_proxy_permissions', NOW()),
                    ('auth', '0012_alter_user_first_name_max_length', NOW()),
                    ('sessions', '0001_initial', NOW()),
                    ('accounts', '0001_initial', NOW()),
                    ('accounts', '0002_contact', NOW()),
                    ('accounts', '0003_contact_responded_by_contact_response_date_and_more', NOW()),
                    ('events', '0001_initial', NOW()),
                    ('events', '0002_subevent_cover_image', NOW()),
                    ('events', '0003_review_likes', NOW()),
                    ('events', '0004_remove_review_likes', NOW()),
                    ('bookings', '0001_initial', NOW()),
                    ('chat', '0001_initial', NOW())
                ON CONFLICT DO NOTHING;
                """)
                print("Marked migrations as applied")
            else:
                print("django_migrations table doesn't exist yet")
    except Exception as e:
        print(f"Error marking migrations as applied: {e}")
        raise

if __name__ == "__main__":
    success = fix_database()
    sys.exit(0 if success else 1)
