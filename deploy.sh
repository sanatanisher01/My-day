#!/bin/bash
# Deployment script for MyDay application
# This script helps with deploying to GitHub and Render

# Set colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}     MyDay Deployment Script     ${NC}"
echo -e "${BLUE}=========================================${NC}"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "\n${YELLOW}Checking prerequisites...${NC}"

if ! command_exists git; then
    echo -e "${RED}Error: Git is not installed. Please install Git and try again.${NC}"
    exit 1
fi

# Check if .git directory exists
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}Git repository not initialized. Initializing...${NC}"
    git init
    git remote add origin https://github.com/sanatanisher01/My-day.git
    echo -e "${GREEN}Git repository initialized and remote added.${NC}"
else
    echo -e "${GREEN}Git repository already initialized.${NC}"
    # Check if remote exists
    if ! git remote | grep -q "origin"; then
        echo -e "${YELLOW}Remote 'origin' not found. Adding...${NC}"
        git remote add origin https://github.com/sanatanisher01/My-day.git
        echo -e "${GREEN}Remote 'origin' added.${NC}"
    else
        echo -e "${GREEN}Remote 'origin' already exists.${NC}"
    fi
fi

# Collect static files
echo -e "\n${YELLOW}Collecting static files...${NC}"
python manage.py collectstatic --noinput
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Static files collected successfully.${NC}"
else
    echo -e "${RED}Error collecting static files. Continuing anyway...${NC}"
fi

# Make migrations
echo -e "\n${YELLOW}Making migrations...${NC}"
python manage.py makemigrations
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Migrations created successfully.${NC}"
else
    echo -e "${RED}Error creating migrations. Continuing anyway...${NC}"
fi

# Apply migrations
echo -e "\n${YELLOW}Applying migrations...${NC}"
python manage.py migrate
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Migrations applied successfully.${NC}"
else
    echo -e "${RED}Error applying migrations. Continuing anyway...${NC}"
fi

# Add all files to Git
echo -e "\n${YELLOW}Adding files to Git...${NC}"
git add .
echo -e "${GREEN}Files added to Git.${NC}"

# Prompt for commit message
echo -e "\n${YELLOW}Enter commit message:${NC}"
read -p "> " commit_message

if [ -z "$commit_message" ]; then
    commit_message="Update application $(date +"%Y-%m-%d %H:%M:%S")"
    echo -e "${YELLOW}Using default commit message: ${commit_message}${NC}"
fi

# Commit changes
echo -e "\n${YELLOW}Committing changes...${NC}"
git commit -m "$commit_message"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Changes committed successfully.${NC}"
else
    echo -e "${RED}Error committing changes. Exiting.${NC}"
    exit 1
fi

# Push to GitHub
echo -e "\n${YELLOW}Pushing to GitHub...${NC}"
git push origin master
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Changes pushed to GitHub successfully.${NC}"
else
    echo -e "${RED}Error pushing to GitHub. Please check your credentials and try again.${NC}"
    exit 1
fi

# Deployment to Render
echo -e "\n${YELLOW}Deployment to Render${NC}"
echo -e "${BLUE}----------------------------------------${NC}"
echo -e "${YELLOW}Your code has been pushed to GitHub.${NC}"
echo -e "${YELLOW}To deploy to Render, follow these steps:${NC}"
echo -e "${BLUE}1. Go to your Render dashboard: https://dashboard.render.com${NC}"
echo -e "${BLUE}2. Select your web service${NC}"
echo -e "${BLUE}3. Click 'Manual Deploy'${NC}"
echo -e "${BLUE}4. Select 'Clear build cache & deploy'${NC}"
echo -e "${BLUE}----------------------------------------${NC}"

# Print success message
echo -e "\n${GREEN}Deployment process completed successfully!${NC}"
echo -e "${GREEN}Your application is now ready to be deployed on Render.${NC}"
echo -e "${BLUE}=========================================${NC}"
