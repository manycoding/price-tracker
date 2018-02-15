import os
from celery.schedules import crontab

broker_url = os.environ['CLOUDAMQP_URL']
beat_schedule = {
    'update_price_data': {
        'task': 'pt.tasks.update_price_data',
        # 'schedule': crontab()
        'schedule': crontab(hour=23, minute=00)
    },
}
broker_pool_limit = 1
task_serializer = "json"
