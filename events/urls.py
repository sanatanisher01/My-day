from django.urls import path
from . import views
from . import manager_views
from . import fallback_views

# Try to import the models to check if the database is set up
try:
    from .models import Event
    DATABASE_READY = True
except Exception:
    DATABASE_READY = False

# Choose between regular views and fallback views based on database status
if DATABASE_READY:
    urlpatterns = [
        path('', views.home, name='home'),
        path('list/', views.event_list, name='event_list'),
        path('<slug:slug>/', views.event_detail, name='event_detail'),

    # Manager routes
    path('manager/dashboard/', manager_views.manager_dashboard, name='manager_dashboard'),
    path('manager/events/', manager_views.manager_events, name='manager_events'),
    path('manager/events/<slug:slug>/analytics/', manager_views.manager_event_detail, name='manager_event_detail'),
    path('manager/events/create/', views.create_event, name='create_event'),
    path('manager/events/<slug:slug>/edit/', views.edit_event, name='edit_event'),
    path('manager/events/<slug:slug>/delete/', views.delete_event, name='delete_event'),

    # Sub-events
    path('manager/events/<slug:event_slug>/sub-events/create/', views.create_sub_event, name='create_sub_event'),
    path('manager/sub-events/<int:sub_event_id>/edit/', views.edit_sub_event, name='edit_sub_event'),
    path('manager/sub-events/<int:sub_event_id>/delete/', views.delete_sub_event, name='delete_sub_event'),

    # Categories
    path('manager/sub-events/<int:sub_event_id>/categories/create/', views.create_category, name='create_category'),
    path('manager/categories/<int:category_id>/edit/', views.edit_category, name='edit_category'),
    path('manager/categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),

    # Gallery
    path('manager/events/<slug:slug>/gallery/', views.event_gallery, name='event_gallery'),
    path('manager/events/<slug:slug>/gallery/add/', views.add_event_image, name='add_event_image'),
    path('manager/gallery/image/<int:image_id>/delete/', views.delete_event_image, name='delete_event_image'),

    # Reviews
    path('events/<slug:slug>/review/', views.add_review, name='add_review'),
    # Like functionality removed
]
else:
    # Fallback urlpatterns when database is not ready
    urlpatterns = [
        path('', fallback_views.fallback_event_list, name='home'),
        path('list/', fallback_views.fallback_event_list, name='event_list'),
        path('<slug:slug>/', fallback_views.fallback_event_detail, name='event_detail'),

        # All other paths redirect to the fallback event list
        path('manager/dashboard/', fallback_views.fallback_event_list),
        path('manager/events/', fallback_views.fallback_event_list),
        path('manager/events/<slug:slug>/analytics/', fallback_views.fallback_event_list),
        path('manager/events/create/', fallback_views.fallback_event_list),
        path('manager/events/<slug:slug>/edit/', fallback_views.fallback_event_list),
        path('manager/events/<slug:slug>/delete/', fallback_views.fallback_event_list),
        path('manager/events/<slug:event_slug>/sub-events/create/', fallback_views.fallback_event_list),
        path('manager/sub-events/<int:sub_event_id>/edit/', fallback_views.fallback_event_list),
        path('manager/sub-events/<int:sub_event_id>/delete/', fallback_views.fallback_event_list),
        path('manager/sub-events/<int:sub_event_id>/categories/create/', fallback_views.fallback_event_list),
        path('manager/categories/<int:category_id>/edit/', fallback_views.fallback_event_list),
        path('manager/categories/<int:category_id>/delete/', fallback_views.fallback_event_list),
        path('manager/events/<slug:slug>/gallery/', fallback_views.fallback_event_list),
        path('manager/events/<slug:slug>/gallery/add/', fallback_views.fallback_event_list),
        path('manager/gallery/image/<int:image_id>/delete/', fallback_views.fallback_event_list),
        path('events/<slug:slug>/review/', fallback_views.fallback_event_detail),
    ]
