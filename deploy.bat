@echo off
REM Deployment script for MyDay application (Windows version)
REM This script helps with deploying to GitHub and Render

echo =========================================
echo      MyDay Deployment Script (Windows)
echo =========================================

REM Check if Git is installed
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Git is not installed. Please install Git and try again.
    exit /b 1
)

REM Check if .git directory exists
if not exist ".git" (
    echo Git repository not initialized. Initializing...
    git init
    git remote add origin https://github.com/sanatanisher01/My-day.git
    echo Git repository initialized and remote added.
) else (
    echo Git repository already initialized.
    REM Check if remote exists
    git remote | findstr "origin" >nul
    if %ERRORLEVEL% NEQ 0 (
        echo Remote 'origin' not found. Adding...
        git remote add origin https://github.com/sanatanisher01/My-day.git
        echo Remote 'origin' added.
    ) else (
        echo Remote 'origin' already exists.
    )
)

REM Collect static files
echo.
echo Collecting static files...
python manage.py collectstatic --noinput
if %ERRORLEVEL% NEQ 0 (
    echo Error collecting static files. Continuing anyway...
)

REM Make migrations
echo.
echo Making migrations...
python manage.py makemigrations
if %ERRORLEVEL% NEQ 0 (
    echo Error creating migrations. Continuing anyway...
)

REM Apply migrations
echo.
echo Applying migrations...
python manage.py migrate
if %ERRORLEVEL% NEQ 0 (
    echo Error applying migrations. Continuing anyway...
)

REM Add all files to Git
echo.
echo Adding files to Git...
git add .
echo Files added to Git.

REM Prompt for commit message
echo.
echo Enter commit message:
set /p commit_message="> "

if "%commit_message%"=="" (
    for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /format:list') do set datetime=%%I
    set commit_message=Update application %datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%
    echo Using default commit message: %commit_message%
)

REM Commit changes
echo.
echo Committing changes...
git commit -m "%commit_message%"
if %ERRORLEVEL% NEQ 0 (
    echo Error committing changes. Exiting.
    exit /b 1
)

REM Push to GitHub
echo.
echo Pushing to GitHub...
git push origin master
if %ERRORLEVEL% NEQ 0 (
    echo Error pushing to GitHub. Please check your credentials and try again.
    exit /b 1
)

REM Deployment to Render
echo.
echo Deployment to Render
echo ----------------------------------------
echo Your code has been pushed to GitHub.
echo To deploy to Render, follow these steps:
echo 1. Go to your Render dashboard: https://dashboard.render.com
echo 2. Select your web service
echo 3. Click 'Manual Deploy'
echo 4. Select 'Clear build cache & deploy'
echo ----------------------------------------

REM Print success message
echo.
echo Deployment process completed successfully!
echo Your application is now ready to be deployed on Render.
echo =========================================

pause
