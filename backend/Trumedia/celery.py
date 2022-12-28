from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

from celery.events.state import State
from celery.schedules import crontab

logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trumedia.settings')

app = Celery('Trumedia')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.control.revoke([
    uuid
    for uuid, _ in
    State().tasks_by_type("Get residential full data")
])

# app.conf.beat_schedule = {
#     'Updating cities': {
#         'task': 'Updating cities',
#         'schedule': crontab(minute='*/5'),
#     },
# }
