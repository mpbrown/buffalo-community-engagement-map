import os
from .base import *

ALLOWED_HOSTS = [
    os.getenv('DJANGO_HOST_URL')
]
DEBUG = False
SECRET_KEY = os.getenv('DJANGO_MAP_SECRET_KEY')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True