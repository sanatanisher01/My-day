"""
URL configuration for myday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from events import views
from myday.views import fallback_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('bookings/', include('bookings.urls')),
    path('chat/', include('chat.urls')),
    # Try the main home page first, fall back to our simple one if it fails
    path('', views.home, name='home'),
]

# Add a fallback pattern for the home page
try:
    # Test if the main home view works
    views.home(None)
except Exception:
    # If it fails, use our fallback view
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('accounts.urls')),
        path('events/', include('events.urls')),
        path('bookings/', include('bookings.urls')),
        path('chat/', include('chat.urls')),
        path('', fallback_home, name='home'),  # Fallback home page
        path('index.html', fallback_home),  # Also handle /index.html
        path('static/', TemplateView.as_view(template_name='index.html')),  # Serve static index.html
    ]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
