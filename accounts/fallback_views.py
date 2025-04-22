"""
Fallback views for the accounts app.
These views are used when the database is not fully set up.
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def fallback_register(request):
    """
    Fallback view for the registration page.
    """
    if request.method == 'POST':
        # Show a message that registration is temporarily unavailable
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MyDay - Registration</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; }
                .navbar { background-color: #4a6da7; }
                .navbar-brand { color: white; font-weight: bold; }
                .nav-link { color: rgba(255,255,255,0.8); }
                .nav-link:hover { color: white; }
                .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
                .alert { margin-top: 20px; }
                .card { border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
                .btn-primary { background-color: #4a6da7; border-color: #4a6da7; }
                .btn-primary:hover { background-color: #3a5a8f; border-color: #3a5a8f; }
                .footer { background-color: #343a40; color: white; padding: 20px 0; margin-top: 40px; }
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">MyDay</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="/">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/events/">Events</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/accounts/login/">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link active" href="/accounts/register/">Register</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="container mt-4">
                <div class="alert alert-warning" role="alert">
                    <h4 class="alert-heading">Registration Temporarily Unavailable</h4>
                    <p>We're sorry, but registration is temporarily unavailable due to maintenance. Please try again later.</p>
                    <hr>
                    <p class="mb-0">You can still browse events and explore the site as a guest.</p>
                </div>
                
                <div class="text-center mt-4">
                    <a href="/" class="btn btn-primary">Return to Home</a>
                    <a href="/accounts/login/" class="btn btn-outline-primary ms-2">Go to Login</a>
                </div>
            </div>

            <footer class="footer mt-5">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6">
                            <h5>MyDay Event Management</h5>
                            <p>Your one-stop solution for event booking and management.</p>
                        </div>
                        <div class="col-md-6 text-md-end">
                            <h5>Contact Us</h5>
                            <p>GLA University, Mathura<br>Email: contact@myday.com</p>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <p>&copy; 2025 MyDay. All rights reserved.</p>
                    </div>
                </div>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """)
    
    # For GET requests, let the original view handle it
    return None

def fallback_login(request):
    """
    Fallback view for the login page.
    """
    if request.method == 'POST':
        # Show a message that login is temporarily unavailable
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MyDay - Login</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; }
                .navbar { background-color: #4a6da7; }
                .navbar-brand { color: white; font-weight: bold; }
                .nav-link { color: rgba(255,255,255,0.8); }
                .nav-link:hover { color: white; }
                .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
                .alert { margin-top: 20px; }
                .card { border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
                .btn-primary { background-color: #4a6da7; border-color: #4a6da7; }
                .btn-primary:hover { background-color: #3a5a8f; border-color: #3a5a8f; }
                .footer { background-color: #343a40; color: white; padding: 20px 0; margin-top: 40px; }
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">MyDay</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="/">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/events/">Events</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link active" href="/accounts/login/">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/accounts/register/">Register</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="container mt-4">
                <div class="alert alert-warning" role="alert">
                    <h4 class="alert-heading">Login Temporarily Unavailable</h4>
                    <p>We're sorry, but login is temporarily unavailable due to maintenance. Please try again later.</p>
                    <hr>
                    <p class="mb-0">You can still browse events and explore the site as a guest.</p>
                </div>
                
                <div class="text-center mt-4">
                    <a href="/" class="btn btn-primary">Return to Home</a>
                    <a href="/events/" class="btn btn-outline-primary ms-2">Browse Events</a>
                </div>
            </div>

            <footer class="footer mt-5">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6">
                            <h5>MyDay Event Management</h5>
                            <p>Your one-stop solution for event booking and management.</p>
                        </div>
                        <div class="col-md-6 text-md-end">
                            <h5>Contact Us</h5>
                            <p>GLA University, Mathura<br>Email: contact@myday.com</p>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <p>&copy; 2025 MyDay. All rights reserved.</p>
                    </div>
                </div>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """)
    
    # For GET requests, let the original view handle it
    return None
