from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(8)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Some Feedback",
        f"\t{message}\n\nThank you!",
        "jstrickler@gmail.com",
        [email_address],
        fail_silently=False,
    )