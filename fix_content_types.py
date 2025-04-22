"""
Script to specifically fix content type issues in the database.
This script directly fixes the null values in the django_content_type table.
"""
import os
import sys
import django
from django.db import connection

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

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
                # First, update any null names in content types
                cursor.execute("""
                UPDATE django_content_type 
                SET name = app_label || '_' || model 
                WHERE name IS NULL;
                """)
                print("Fixed null names in content types")
                
                # Then, check if there are still null values
                cursor.execute("""
                SELECT COUNT(*) FROM django_content_type WHERE name IS NULL;
                """)
                null_count = cursor.fetchone()[0]
                
                if null_count > 0:
                    print(f"Found {null_count} content types with null names after update")
                    
                    # Get the problematic rows
                    cursor.execute("""
                    SELECT id, app_label, model FROM django_content_type WHERE name IS NULL;
                    """)
                    null_rows = cursor.fetchall()
                    
                    # Update each row individually
                    for row in null_rows:
                        row_id, app_label, model = row
                        name = f"{app_label}_{model}"
                        cursor.execute("""
                        UPDATE django_content_type 
                        SET name = %s 
                        WHERE id = %s;
                        """, [name, row_id])
                        print(f"Fixed content type {row_id}: {app_label}.{model} -> {name}")
                
                # Verify all content types have names
                cursor.execute("""
                SELECT COUNT(*) FROM django_content_type WHERE name IS NULL;
                """)
                null_count = cursor.fetchone()[0]
                
                if null_count == 0:
                    print("All content types now have names")
                else:
                    print(f"WARNING: Still found {null_count} content types with null names")
            else:
                print("django_content_type table doesn't exist yet")
        
        return True
    except Exception as e:
        print(f"Error fixing content types: {e}")
        return False

if __name__ == "__main__":
    success = fix_content_types()
    sys.exit(0 if success else 1)
