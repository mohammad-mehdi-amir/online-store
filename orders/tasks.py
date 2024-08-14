
# order/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .models import EmailQueue
import os
from dotenv import load_dotenv
@shared_task
def send_order_email(order_link):

    emails = EmailQueue.objects.filter(ready_to_send=True)
    for email_obj in emails:
        if email_obj.ready_to_send:
            send_mail(
                "سفارش جدید ثبت شد",
                f"مشاهده در لینک زیر \n {order_link}",  # شما می‌توانید این متن را بر اساس نیاز خود تغییر دهید.
                from_email=os.getenv('DEFAULT_FROM_EMAIL'),
                recipient_list=[email_obj.email],
                fail_silently=False,
            )

