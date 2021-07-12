import environ

env = environ.Env()

from .base import *

DATABASES['default'] = env.db('DATABASE_URL')
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
