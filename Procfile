web: gunicorn price_tracker.wsgi --log-file -
celery: celery worker -A price_tracker -l info --beat -b amqp://pt_admin:password@localhost:5672/myvhost