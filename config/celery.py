# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات محیط برای Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# تنظیمات Celery را از settings.py بارگذاری می‌کند
app.config_from_object('django.conf:settings', namespace='CELERY')

# جستجو و بارگذاری task ها از همه اپلیکیشن‌های Django
app.autodiscover_tasks()
