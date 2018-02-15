from __future__ import absolute_import, unicode_literals
import os
import celeryconfig
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_tracker.settings')
# os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')

app = Celery('price_tracker')

app.config_from_object(celeryconfig)
# app.config_from_envvar('CELERY_CONFIG_MODULE')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
