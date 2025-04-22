"""
Fallback views for the events app.
These views are used when the database is not fully set up.
"""
from django.http import HttpResponse
from django.shortcuts import render

def fallback_event_list(request):
    """
    Fallback view for the event list page.
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MyDay - Events</title>
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
            .card { border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; transition: transform 0.3s; }
            .card:hover { transform: translateY(-5px); }
            .card-img-top { height: 200px; object-fit: cover; }
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
                            <a class="nav-link active" href="/events/">Events</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/login/">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/register/">Register</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-4">
            <h1 class="mb-4">Upcoming Events</h1>
            
            <div class="row">
                <div class="col-md-4">
                    <div class="card">
                        <img src="https://via.placeholder.com/300x200?text=Conference" class="card-img-top" alt="Conference">
                        <div class="card-body">
                            <h5 class="card-title">Annual Tech Conference</h5>
                            <p class="card-text">Join us for the annual tech conference featuring speakers from around the world.</p>
                            <p><strong>Date:</strong> June 15-17, 2025</p>
                            <p><strong>Location:</strong> GLA University, Mathura</p>
                            <a href="#" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card">
                        <img src="https://via.placeholder.com/300x200?text=Workshop" class="card-img-top" alt="Workshop">
                        <div class="card-body">
                            <h5 class="card-title">Web Development Workshop</h5>
                            <p class="card-text">Learn the latest web development techniques in this hands-on workshop.</p>
                            <p><strong>Date:</strong> July 5, 2025</p>
                            <p><strong>Location:</strong> GLA University, Mathura</p>
                            <a href="#" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card">
                        <img src="https://via.placeholder.com/300x200?text=Seminar" class="card-img-top" alt="Seminar">
                        <div class="card-body">
                            <h5 class="card-title">AI in Education Seminar</h5>
                            <p class="card-text">Explore how artificial intelligence is transforming education.</p>
                            <p><strong>Date:</strong> August 10, 2025</p>
                            <p><strong>Location:</strong> GLA University, Mathura</p>
                            <a href="#" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-4">
                <p>These are sample events. The actual events will be available once the database is fully set up.</p>
                <a href="/" class="btn btn-outline-primary">Return to Home</a>
            </div>
        </div>

        <footer class="footer">
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
    """
    return HttpResponse(html)

def fallback_event_detail(request, event_id=None):
    """
    Fallback view for the event detail page.
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MyDay - Event Details</title>
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
            .event-header { background-color: #4a6da7; color: white; padding: 40px 0; }
            .event-details { background-color: white; padding: 30px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .event-image { width: 100%; height: 400px; object-fit: cover; border-radius: 5px; }
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
                            <a class="nav-link" href="/accounts/register/">Register</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="event-header">
            <div class="container">
                <h1>Annual Tech Conference</h1>
                <p class="lead">Join us for the annual tech conference featuring speakers from around the world.</p>
            </div>
        </div>

        <div class="container mt-4">
            <div class="row">
                <div class="col-md-8">
                    <div class="event-details">
                        <img src="https://via.placeholder.com/800x400?text=Conference" class="event-image mb-4" alt="Conference">
                        
                        <h2>Event Details</h2>
                        <p>Join us for the annual tech conference featuring speakers from around the world. This three-day event will cover the latest trends in technology, including artificial intelligence, blockchain, cloud computing, and more.</p>
                        
                        <h3 class="mt-4">Schedule</h3>
                        <ul>
                            <li><strong>Day 1:</strong> Opening keynote, AI workshops, networking lunch</li>
                            <li><strong>Day 2:</strong> Blockchain sessions, panel discussions, evening reception</li>
                            <li><strong>Day 3:</strong> Cloud computing workshops, closing keynote, awards ceremony</li>
                        </ul>
                        
                        <h3 class="mt-4">Speakers</h3>
                        <p>We have an impressive lineup of speakers from leading tech companies and universities around the world.</p>
                        
                        <div class="mt-4">
                            <a href="/events/" class="btn btn-primary">Back to Events</a>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="event-details">
                        <h3>Event Information</h3>
                        <p><strong>Date:</strong> June 15-17, 2025</p>
                        <p><strong>Time:</strong> 9:00 AM - 5:00 PM</p>
                        <p><strong>Location:</strong> GLA University, Mathura</p>
                        <p><strong>Price:</strong> ₹999</p>
                        <p><strong>Capacity:</strong> 500 attendees</p>
                        
                        <div class="mt-4">
                            <a href="/accounts/login/" class="btn btn-primary w-100">Book Now</a>
                        </div>
                        
                        <div class="mt-3">
                            <p class="text-muted">You need to be logged in to book this event.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-4">
                <p>This is a sample event. The actual event details will be available once the database is fully set up.</p>
                <a href="/" class="btn btn-outline-primary">Return to Home</a>
            </div>
        </div>

        <footer class="footer">
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
    """
    return HttpResponse(html)
