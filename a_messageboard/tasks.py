from celery import shared_task
from django.core.mail import EmailMessage
from .models import MessageBoard
from django.template.loader import render_to_string
from django.utils import timezone
from celery.schedules import crontab
from a_core.celery import app

@shared_task(bind=True, max_retries=3, name='email_notification')
def send_email_task(self, subject, body, email):
    email = EmailMessage(subject, body, to=[email])
    email.send()


@shared_task(bind=True, max_retries=3, name='monthly_newsletter')
def send_newsletter():
    subject = 'Monthly Newsletter'

    subscribesrs = MessageBoard.objects.get(id=1).subscribers.all()

    for subscriber in subscribesrs:
        body = render_to_string('a_messageboard/newsletter.html', {'name': subscriber.profile.name})

        email = EmailMessage(subject, body, to=[subscriber.email])
        email.content_subtype = 'html'
        email.send()

    current_month = timezone.now().strftime('%B')

    return f"{current_month} Newsletter to {subscribesrs.count()} subscribers"


# add "send_newsletter" task to the beat schedule
app.conf.beat_schedule = {
    "birthday-task": {
        "task": "tasks.send_newsletter",
        "schedule": crontab(hour=7, minute=0)
    }
}