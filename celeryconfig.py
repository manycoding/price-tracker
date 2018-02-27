import os
from celery.schedules import crontab

broker_url = os.environ['CLOUDAMQP_URL']
crontab_schedule = os.environ.get('CELERY_SCHEDULE', '*/1440')

beat_schedule = {
    'update_price_data': {
        'task': 'pt.tasks.update_price_data',
        'schedule': crontab(minute=crontab_schedule)
    },
}
broker_pool_limit = 1
task_serializer = "json"
