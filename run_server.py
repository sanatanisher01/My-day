#!/usr/bin/env python
"""
Script to run the MyDay application on a server.
"""
import os
import sys
import subprocess
import argparse

def check_dependencies():
    """Check if all dependencies are installed."""
    print("Checking dependencies...")
    try:
        import django
        import dotenv
        import waitress
        import whitenoise
        import cloudinary
        print("All dependencies are installed.")
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Installing dependencies...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        return False

def collect_static():
    """Collect static files."""
    print("Collecting static files...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings_prod')
    subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'])

def migrate_database():
    """Run database migrations."""
    print("Running database migrations...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings_prod')
    subprocess.run([sys.executable, 'manage.py', 'migrate'])

def run_development_server(port):
    """Run the Django development server."""
    print(f"Starting development server on port {port}...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings')
    subprocess.run([sys.executable, 'manage.py', 'runserver', f'0.0.0.0:{port}'])

def run_production_server(port, workers=3):
    """Run the production server using Gunicorn on Unix or Waitress on Windows."""
    print(f"Starting production server on port {port} with {workers} workers...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myday.settings_prod')

    # Collect static files and run migrations before starting the server
    collect_static()
    migrate_database()

    # Check if we're on Windows
    if os.name == 'nt':
        print("Detected Windows OS, using Waitress server...")
        # Use Waitress on Windows
        from waitress import serve
        from myday.wsgi import application
        print(f"Server is running at http://localhost:{port}")
        serve(application, host='0.0.0.0', port=port, threads=workers*2)
    else:
        print("Detected Unix-like OS, using Gunicorn server...")
        # Start Gunicorn on Unix-like systems
        subprocess.run([
            'gunicorn',
            'myday.wsgi:application',
            f'--bind=0.0.0.0:{port}',
            f'--workers={workers}',
            '--log-level=info',
            '--access-logfile=-',
            '--error-logfile=-',
        ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the MyDay application server')
    parser.add_argument('--mode', choices=['dev', 'prod'], default='prod',
                        help='Server mode: development or production (default: prod)')
    parser.add_argument('--port', type=int, default=8000,
                        help='Port to run the server on (default: 8000)')
    parser.add_argument('--workers', type=int, default=3,
                        help='Number of worker processes for production mode (default: 3)')

    args = parser.parse_args()

    # Check dependencies first
    check_dependencies()

    if args.mode == 'dev':
        run_development_server(args.port)
    else:
        run_production_server(args.port, args.workers)
