from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_template_email(subject, template_name, context, recipient_list, from_email=None, retry_count=2):
    """
    Send an email using a template with retry logic.

    Args:
        subject (str): Email subject
        template_name (str): Name of the HTML template to use (without .html extension)
        context (dict): Context data for the template
        recipient_list (list): List of recipient email addresses
        from_email (str, optional): Sender email address. Defaults to settings.EMAIL_HOST_USER.
        retry_count (int, optional): Number of retry attempts if sending fails. Defaults to 2.

    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    import logging
    logger = logging.getLogger(__name__)

    if from_email is None:
        from_email = settings.EMAIL_HOST_USER

    # Add site URL to context
    if 'site_url' not in context:
        context['site_url'] = 'http://127.0.0.1:8080'

    # Render HTML content
    try:
        html_content = render_to_string(f'emails/{template_name}.html', context)
    except Exception as e:
        logger.error(f"Error rendering email template '{template_name}': {e}")
        return False

    # Create plain text content
    text_content = strip_tags(html_content)

    # Create email
    email = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        recipient_list
    )

    # Attach HTML content
    email.attach_alternative(html_content, "text/html")

    # Try sending with retries
    for attempt in range(retry_count + 1):
        try:
            # Send email
            email.send()
            return True
        except Exception as e:
            if attempt < retry_count:
                # Log retry attempt
                logger.warning(f"Email sending failed (attempt {attempt+1}/{retry_count+1}): {e}. Retrying...")
                import time
                time.sleep(1)  # Wait 1 second before retrying
            else:
                # Log final failure
                logger.error(f"Error sending email after {retry_count+1} attempts: {e}")
                return False

def send_booking_confirmation(booking):
    """Send booking confirmation email to user"""
    subject = f"Booking Confirmation - {booking.event.name}"
    template_name = "booking_confirmation"
    context = {
        'booking': booking,
        'user': booking.user,
        'event': booking.event,
        'sub_events': booking.sub_event_bookings.all(),
    }
    recipient_list = [booking.user.email]

    return send_template_email(subject, template_name, context, recipient_list)

def send_booking_approved(booking):
    """Send booking approved email to user"""
    subject = f"Booking Approved - {booking.event.name}"
    template_name = "booking_approved"
    context = {
        'booking': booking,
        'user': booking.user,
        'event': booking.event,
    }
    recipient_list = [booking.user.email]

    return send_template_email(subject, template_name, context, recipient_list)

def send_booking_rejected(booking):
    """Send booking rejected email to user"""
    subject = f"Booking Update - {booking.event.name}"
    template_name = "booking_rejected"
    context = {
        'booking': booking,
        'user': booking.user,
        'event': booking.event,
    }
    recipient_list = [booking.user.email]

    return send_template_email(subject, template_name, context, recipient_list)

def send_welcome_email(user):
    """Send welcome email to new user"""
    subject = "Welcome to MyDay!"
    template_name = "welcome_email"
    context = {
        'user': user,
    }
    recipient_list = [user.email]

    return send_template_email(subject, template_name, context, recipient_list)

def send_password_reset(user, reset_url):
    """Send password reset email"""
    subject = "Reset Your MyDay Password"
    template_name = "password_reset"
    context = {
        'user': user,
        'reset_url': reset_url,
    }
    recipient_list = [user.email]

    return send_template_email(subject, template_name, context, recipient_list)

def send_contact_notification(contact):
    """Send notification to managers about new contact message"""
    subject = f"New Contact Message: {contact.subject}"
    template_name = "contact_notification"
    context = {
        'contact': contact,
    }

    # Get all manager emails
    from django.contrib.auth.models import User
    from accounts.models import UserProfile

    manager_emails = User.objects.filter(
        profile__is_manager=True
    ).values_list('email', flat=True)

    # If no managers, send to the default email
    if not manager_emails:
        manager_emails = [settings.EMAIL_HOST_USER]

    return send_template_email(subject, template_name, context, list(manager_emails))
