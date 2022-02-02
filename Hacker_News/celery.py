import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hacker_News.settings')

app = Celery('Hacker_News')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-day': {
        'task': 'apps.news.tasks.clear_qs_every_day',
        'schedule': crontab(hour=4, minute=26),
    }
}
app.autodiscover_tasks()
