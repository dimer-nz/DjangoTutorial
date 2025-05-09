from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_contact_email(email, subject, message):
    full_message = f"""
        Received message below from {email}, {subject}
        ________________________


        {message}
        """
    send_mail(
        subject="Received contact form submission",
        message=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.NOTIFY_EMAIL],
    )