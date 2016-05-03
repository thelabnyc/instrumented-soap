import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
]

SECRET_KEY = 'li0$-gnv)76g$yf7p@(cg-^_q7j6df5cx$o-gsef5hd68phj!4'

SOAP_PROXY_URL = None
