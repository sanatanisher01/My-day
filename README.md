# MyDay - Event Booking & Management

MyDay is a comprehensive event booking and management platform built with Django. It allows users to browse events, make bookings, and communicate with event managers.

## Features

- User authentication and profiles
- Event browsing and searching
- Booking management
- Real-time chat between users and event managers
- Admin dashboard for event managers
- Responsive design using Bootstrap 5
- Cloudinary integration for media storage

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/sanatanisher01/My-day.git
   cd My-day
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and fill in your credentials:
   ```
   cp .env.example .env
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at http://localhost:8000

## Deployment to Render

1. Create a new Web Service on Render:
   - Connect your GitHub repository
   - Select the repository: `sanatanisher01/My-day`
   - Select the branch: `master`
   - Set the build command to: `chmod +x render_build.sh && ./render_build.sh`
   - Set the start command to: `chmod +x startup.sh && ./startup.sh gunicorn myday.wsgi:application --workers=1 --threads=8 --timeout=0`
   - Select the "Free" plan

2. Set Environment Variables:
   - `DJANGO_SECRET_KEY`: Generate a secure random key
   - `DJANGO_DEBUG`: Set to "False"
   - `ALLOWED_HOSTS`: Include your Render domain
   - `RENDER`: Set to "true"
   - `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
   - `CLOUDINARY_API_KEY`: Your Cloudinary API key
   - `CLOUDINARY_API_SECRET`: Your Cloudinary API secret
   - `EMAIL_HOST_USER`: Your email address
   - `EMAIL_HOST_PASSWORD`: Your email app password

3. Create a PostgreSQL Database on Render and link it to your web service.

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Quick Deployment

Use the provided deployment scripts:

- On Linux/Mac: `./deploy.sh`
- On Windows: `deploy.bat`

These scripts will help you push your code to GitHub and provide instructions for deploying to Render.

## Environment Variables

The application uses environment variables for configuration. See `.env.example` for available options.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django
- Bootstrap 5
- Cloudinary
- GSAP for animations
- SweetAlert2 for better alerts
