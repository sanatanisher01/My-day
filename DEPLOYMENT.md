# Deployment Guide for MyDay

This guide provides instructions for deploying the MyDay application to GitHub and Render.

## Prerequisites

- Git installed on your local machine
- GitHub account
- Render account

## Pushing to GitHub

### Initial Setup (First Time Only)

1. Initialize a Git repository (if not already done):
   ```bash
   git init
   ```

2. Add your GitHub repository as a remote:
   ```bash
   git remote add origin https://github.com/sanatanisher01/My-day.git
   ```

### Regular Deployment

1. Add all files to Git:
   ```bash
   git add .
   ```

2. Commit your changes:
   ```bash
   git commit -m "Your commit message here"
   ```

3. Push to GitHub:
   ```bash
   git push origin master
   ```

## Deploying to Render

### Initial Setup (First Time Only)

1. Create a new Web Service on Render:
   - Go to your Render dashboard
   - Click "New" and select "Web Service"
   - Connect your GitHub repository
   - Select the repository: `sanatanisher01/My-day`
   - Select the branch: `master`
   - Give your service a name (e.g., `myday`)
   - Select "Python" as the runtime
   - Set the build command to: `chmod +x render_build.sh && ./render_build.sh`
   - Set the start command to: `chmod +x startup.sh && ./startup.sh gunicorn myday.wsgi:application --workers=1 --threads=8 --timeout=0`
   - Select the "Free" plan
   - Click "Create Web Service"

2. Set Environment Variables:
   - Go to your web service settings
   - Add the following environment variables:
     - `DJANGO_SECRET_KEY`: Generate a secure random key
     - `DJANGO_DEBUG`: Set to "False"
     - `ALLOWED_HOSTS`: Include your Render domain (e.g., `myday.onrender.com,localhost,127.0.0.1`)
     - `RENDER`: Set to "true"
     - `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
     - `CLOUDINARY_API_KEY`: Your Cloudinary API key
     - `CLOUDINARY_API_SECRET`: Your Cloudinary API secret
     - `EMAIL_HOST_USER`: Your email address
     - `EMAIL_HOST_PASSWORD`: Your email app password

3. Create a PostgreSQL Database:
   - Go to the "New" menu and select "PostgreSQL"
   - Give your database a name (e.g., `myday-db`)
   - Select the "Free" plan
   - Click "Create Database"

4. Link the Database to Your Web Service:
   - Go to your web service settings
   - Add a new environment variable: `DATABASE_URL`
   - Set its value to the Internal Database URL from your PostgreSQL database

### Regular Deployment

After pushing changes to GitHub, you can deploy to Render in one of two ways:

#### Option 1: Automatic Deployment

If you've enabled automatic deployments, Render will automatically deploy your application whenever you push to the configured branch.

#### Option 2: Manual Deployment

1. Go to your Render dashboard
2. Select your web service
3. Click "Manual Deploy"
4. Select "Clear build cache & deploy"

## Troubleshooting

### Common Issues

1. **500 Server Error**:
   - Check the Render logs for specific error messages
   - Verify that all environment variables are set correctly
   - Make sure the database is properly configured

2. **Database Migration Issues**:
   - Use the `fix_database.py` script to fix database issues
   - Check if there are conflicting migrations

3. **Static Files Not Loading**:
   - Make sure WhiteNoise is properly configured
   - Verify that static files are collected during the build process

### Useful Commands

- Run the deployment script:
  ```bash
  ./deploy.sh
  ```

- Check the status of your Render service:
  ```bash
  curl https://your-app-name.onrender.com/
  ```

## Important Files

- `render_build.sh`: Script that runs during the build process on Render
- `startup.sh`: Script that runs when the application starts on Render
- `fix_database.py`: Script to fix database issues
- `deploy.sh`: Script to help with deployment to GitHub and Render

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [GitHub Documentation](https://docs.github.com/en)
