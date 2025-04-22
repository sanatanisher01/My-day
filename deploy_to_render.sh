#!/bin/bash
# This script helps with manual deployment to Render
# Run this script if you're having issues with the automatic deployment

echo "=== Starting manual deployment to Render ==="

# Push latest changes to GitHub
echo "=== Pushing latest changes to GitHub ==="
git add .
git commit -m "Manual deployment update" || true
git push origin master

# Instructions for Render deployment
echo ""
echo "=== Next steps ==="
echo "1. Go to your Render dashboard"
echo "2. Select your web service"
echo "3. Click 'Manual Deploy'"
echo "4. Select 'Clear build cache & deploy'"
echo ""
echo "=== Deployment tips ==="
echo "- Check the build logs for any errors"
echo "- Make sure all environment variables are set correctly"
echo "- If you're still having issues, try creating a new service"
echo ""
echo "=== Environment variables needed ==="
echo "- DJANGO_SECRET_KEY"
echo "- ALLOWED_HOSTS (should include your Render domain)"
echo "- CLOUDINARY_CLOUD_NAME"
echo "- CLOUDINARY_API_KEY"
echo "- CLOUDINARY_API_SECRET"
echo "- EMAIL_HOST_USER"
echo "- EMAIL_HOST_PASSWORD"
echo ""
echo "=== Script completed ==="
