web: gunicorn price_tracker.wsgi --log-file -
celery: celery worker --app price_tracker --loglevel info --beat