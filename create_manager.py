import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile

def create_manager():
    try:
        # Check if user already exists
        if User.objects.filter(username='aryanayusharushdevang').exists():
            user = User.objects.get(username='aryanayusharushdevang')
            print(f'User {user.username} already exists')
            
            # Update password
            user.set_password('Aditya@010')
            user.save()
            print(f'Password updated for user {user.username}')
        else:
            # Create user
            user = User.objects.create_user(
                username='aryanayusharushdevang',
                email='aryansanatani01@gmail.com',
                password='Aditya@010'
            )
            user.first_name = 'Aryan'
            user.last_name = 'Manager'
            user.save()
            print(f'User {user.username} created successfully')
        
        # Get or create profile
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.is_manager = True
        profile.save()
        
        print(f'User {user.username} is now a manager')
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    create_manager()
