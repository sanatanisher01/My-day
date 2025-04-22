"""
Views for the MyDay project.
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

def fallback_home(request):
    """
    Fallback home page view.
    This is used when the main home page view fails.
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MyDay - Welcome</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { color: #4a6da7; }
            .container { max-width: 800px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
            .btn { display: inline-block; padding: 10px 20px; background-color: #4a6da7; color: white; text-decoration: none; border-radius: 5px; }
            .btn:hover { background-color: #3a5a8f; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to MyDay</h1>
            <p>Your one-stop solution for event booking and management.</p>
            <p>Browse our events, book your favorites, and manage your bookings all in one place.</p>
            <p>
                <a href="/events/" class="btn">Browse Events</a>
                <a href="/accounts/login/" class="btn">Login</a>
                <a href="/accounts/register/" class="btn">Register</a>
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
