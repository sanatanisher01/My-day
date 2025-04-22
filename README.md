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
   git clone <repository-url>
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

1. Create a new Web Service on Render.

2. Connect your GitHub repository.

3. Configure the following settings:
   - **Name**: myday (or your preferred name)
   - **Environment**: Python
   - **Region**: Choose the region closest to your users
   - **Branch**: main (or your deployment branch)
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn myday.wsgi:application`

4. Add the following environment variables:
   - `DJANGO_SECRET_KEY`: Generate a secure random key
   - `DJANGO_DEBUG`: Set to "False"
   - `ALLOWED_HOSTS`: Your Render domain (e.g., `your-app.onrender.com`)
   - `DATABASE_URL`: This will be automatically added if you create a PostgreSQL database on Render
   - `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
   - `CLOUDINARY_API_KEY`: Your Cloudinary API key
   - `CLOUDINARY_API_SECRET`: Your Cloudinary API secret
   - `EMAIL_HOST_USER`: Your email address
   - `EMAIL_HOST_PASSWORD`: Your email app password

5. Create a PostgreSQL database on Render and link it to your web service.

6. Deploy your application.

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
