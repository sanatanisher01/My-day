"""
Comprehensive script to initialize the database from scratch.
This script will create all necessary tables and populate initial data.
"""
import os
import sys
import django
from django.db import connection, transaction
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

def initialize_database():
    """Initialize the database from scratch."""
    print("Starting comprehensive database initialization...")
    
    try:
        # Fix content types
        fix_content_types()
        
        # Create necessary tables
        create_tables()
        
        # Create initial data
        create_initial_data()
        
        # Mark migrations as applied
        mark_migrations_as_applied()
        
        print("Database initialization completed successfully.")
        return True
    except Exception as e:
        print(f"Error initializing database: {e}")
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
                cursor.execute("""
                INSERT INTO django_content_type (app_label, model, name)
                VALUES 
                    ('admin', 'logentry', 'admin_logentry'),
                    ('auth', 'permission', 'auth_permission'),
                    ('auth', 'group', 'auth_group'),
                    ('auth', 'user', 'auth_user'),
                    ('contenttypes', 'contenttype', 'contenttypes_contenttype'),
                    ('sessions', 'session', 'sessions_session'),
                    ('accounts', 'userprofile', 'accounts_userprofile'),
                    ('accounts', 'contact', 'accounts_contact'),
                    ('events', 'category', 'events_category'),
                    ('events', 'event', 'events_event'),
                    ('events', 'subevent', 'events_subevent'),
                    ('events', 'eventimage', 'events_eventimage'),
                    ('events', 'review', 'events_review'),
                    ('bookings', 'booking', 'bookings_booking'),
                    ('bookings', 'discount', 'bookings_discount'),
                    ('chat', 'chatmessage', 'chat_chatmessage')
                ON CONFLICT DO NOTHING;
                """)
                print("Ensured all models have content types")
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
            # Create events_category table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS events_category (
                id bigserial PRIMARY KEY,
                name varchar(100) NOT NULL,
                description text,
                created_at timestamp with time zone NOT NULL,
                updated_at timestamp with time zone NOT NULL
            );
            """)
            print("Created events_category table")
            
            # Create events_event table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS events_event (
                id bigserial PRIMARY KEY,
                name varchar(200) NOT NULL,
                description text NOT NULL,
                location varchar(200) NOT NULL,
                capacity integer NOT NULL,
                price numeric(10, 2) NOT NULL,
                start_date timestamp with time zone NOT NULL,
                end_date timestamp with time zone NOT NULL,
                is_featured boolean NOT NULL,
                cover_image varchar(100),
                created_at timestamp with time zone NOT NULL,
                updated_at timestamp with time zone NOT NULL,
                category_id bigint REFERENCES events_category(id)
            );
            """)
            print("Created events_event table")
            
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

def create_initial_data():
    """Create initial data for the application."""
    print("Creating initial data...")
    
    try:
        # Import models
        from events.models import Category, Event
        from accounts.models import UserProfile
        from django.contrib.auth.models import User
        
        # Create a superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            try:
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                print("Created superuser 'admin'")
            except Exception as e:
                print(f"Error creating superuser: {e}")
        
        # Create event categories if none exist
        if Category.objects.count() == 0:
            try:
                categories = [
                    {
                        'name': 'Conferences',
                        'description': 'Professional gatherings for networking and learning'
                    },
                    {
                        'name': 'Workshops',
                        'description': 'Hands-on learning experiences'
                    },
                    {
                        'name': 'Seminars',
                        'description': 'Educational events focused on specific topics'
                    },
                    {
                        'name': 'Social Events',
                        'description': 'Gatherings for socializing and networking'
                    }
                ]
                
                for category_data in categories:
                    Category.objects.create(
                        name=category_data['name'],
                        description=category_data['description'],
                        created_at=timezone.now(),
                        updated_at=timezone.now()
                    )
                print(f"Created {len(categories)} event categories")
            except Exception as e:
                print(f"Error creating categories: {e}")
        
        # Create sample events if none exist
        if Event.objects.count() == 0:
            try:
                # Get the first category
                category = Category.objects.first()
                if category:
                    # Create a sample event
                    Event.objects.create(
                        name='Sample Conference',
                        description='A sample conference for demonstration purposes',
                        location='Virtual',
                        capacity=100,
                        price=99.99,
                        start_date=timezone.now() + timezone.timedelta(days=30),
                        end_date=timezone.now() + timezone.timedelta(days=32),
                        is_featured=True,
                        category=category,
                        created_at=timezone.now(),
                        updated_at=timezone.now()
                    )
                    print("Created sample event")
            except Exception as e:
                print(f"Error creating sample event: {e}")
    except Exception as e:
        print(f"Error creating initial data: {e}")
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
    success = initialize_database()
    sys.exit(0 if success else 1)
