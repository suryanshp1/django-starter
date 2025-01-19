from django.core.mail import EmailMessage
from .tasks import send_email_task
# import threading

def send_email_thread(subject, body, subscriber):
    email = EmailMessage(subject, body, to=[subscriber.email])
    email.send()

def send_email(message):
    messageboard = message.messageboard
    subscribers = messageboard.subscribers.all()

    for subscriber in subscribers:
        subject = f'New message on {message.author.profile.name}'
        body = f'{message.author.profile.name}: {message.body}\n\nRegards from\n\nMy Message Board'

        # email_thread = threading.Thread(target=send_email_thread, args=(subject, body, subscriber))
        # email_thread.start()

        # email = EmailMessage(subject, body, to=[subscriber.email])
        # email.send()

        send_email_task.delay(subject, body, subscriber.email)