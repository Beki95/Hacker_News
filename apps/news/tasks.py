import datetime
from celery import shared_task

from apps.news.models import News


@shared_task
def clear_qs_every_day() -> str:
    News.objects.filter().update(qs_vote=0)
    return 'ok'
