"""
Custom middleware for the MyDay application.
"""
import sys
import traceback
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

class ErrorHandlingMiddleware:
    """
    Middleware to handle errors gracefully.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            # Log the error
            print(f"Error handling request: {e}")
            traceback.print_exc()
            
            # Create a simple error page
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>MyDay - Temporary Error</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                    h1 {{ color: #d9534f; }}
                    .container {{ max-width: 800px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
                    .error {{ background-color: #f8d7da; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Temporary Error</h1>
                    <div class="error">
                        <p>We're sorry, but there was a temporary error processing your request.</p>
                        <p>Our team has been notified and is working to fix the issue.</p>
                    </div>
                    <p>Please try again later or visit the <a href="/">home page</a>.</p>
                    <p>You can also try accessing the <a href="/events/">events page</a> or the <a href="/accounts/login/">login page</a>.</p>
                </div>
            </body>
            </html>
            """
            
            # Only show error details in debug mode
            if settings.DEBUG:
                error_html += f"""
                <div style="margin-top: 30px; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                    <h3>Error Details (Debug Mode Only)</h3>
                    <pre>{str(e)}</pre>
                    <pre>{traceback.format_exc()}</pre>
                </div>
                """
            
            return HttpResponse(error_html, status=500)
