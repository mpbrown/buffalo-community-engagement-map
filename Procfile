web: gunicorn config.wsgi
worker: celery --app=config worker --loglevel=INFO --without-heartbeat=True