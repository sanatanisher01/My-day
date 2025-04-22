from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import fallback_views

# Try to import the models to check if the database is set up
try:
    from django.contrib.auth.models import User
    DATABASE_READY = True
except Exception:
    DATABASE_READY = False

# Define a custom login view that uses fallback if needed
class SafeLoginView(auth_views.LoginView):
    def post(self, request, *args, **kwargs):
        if not DATABASE_READY:
            fallback_response = fallback_views.fallback_login(request)
            if fallback_response:
                return fallback_response
        return super().post(request, *args, **kwargs)

# Define urlpatterns based on database status
urlpatterns = [
    # Use a custom view for register that checks database status
    path('register/', lambda request, *args, **kwargs:
         fallback_views.fallback_register(request) if request.method == 'POST' and not DATABASE_READY
         else views.register(request, *args, **kwargs),
         name='register'),

    # Use the custom login view
    path('login/', SafeLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('api/booking-analytics/', views.booking_analytics, name='booking_analytics'),
    path('contact/', views.contact, name='contact'),
    path('manager/contacts/', views.manager_contacts, name='manager_contacts'),
    path('manager/contacts/<int:contact_id>/', views.manager_contact_detail, name='manager_contact_detail'),

    # Password reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
