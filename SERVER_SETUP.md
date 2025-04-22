# MyDay Server Setup Guide

This guide explains how to run the MyDay application on a server.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A server with SSH access

## Installation Steps

1. Clone the repository to your server:
   ```
   git clone <your-repository-url>
   cd My-day
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Collect static files and run migrations:
   ```
   python manage.py collectstatic --settings=myday.settings_prod
   python manage.py migrate --settings=myday.settings_prod
   ```

## Running the Server

### Development Mode

For testing purposes, you can run the development server:

```
python run_server.py --mode=dev --port=8000
```

### Production Mode

For production deployment, use Gunicorn:

```
python run_server.py --mode=prod --port=8000 --workers=3
```

Or directly:

```
gunicorn myday.wsgi:application --bind=0.0.0.0:8000 --workers=3
```

## Environment Variables

You may want to set these environment variables for security:

- `DJANGO_SECRET_KEY`: A secure secret key
- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
- `CLOUDINARY_API_KEY`: Your Cloudinary API key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API secret

## Accessing the Application

Once the server is running, you can access the application at:

```
http://your-server-ip:8000
```

## Using a Process Manager

For long-running applications, it's recommended to use a process manager like Supervisor or systemd.

### Example Supervisor Configuration

Create a file `/etc/supervisor/conf.d/myday.conf`:

```
[program:myday]
command=/path/to/venv/bin/gunicorn myday.wsgi:application --bind=0.0.0.0:8000 --workers=3
directory=/path/to/My-day
user=your_user
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/path/to/My-day/logs/gunicorn.log
environment=DJANGO_SETTINGS_MODULE="myday.settings_prod"
```

Then run:

```
supervisorctl reread
supervisorctl update
supervisorctl start myday
```

## Using Nginx as a Reverse Proxy

For production, it's recommended to use Nginx as a reverse proxy in front of Gunicorn.

### Example Nginx Configuration

Create a file `/etc/nginx/sites-available/myday`:

```
server {
    listen 80;
    server_name your-domain.com;

    location /static/ {
        alias /path/to/My-day/staticfiles/;
    }

    location /media/ {
        alias /path/to/My-day/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and restart Nginx:

```
ln -s /etc/nginx/sites-available/myday /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```
