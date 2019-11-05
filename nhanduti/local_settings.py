# coding=utf-8

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nhanduti',
        'USER': 'diagonal',
        'PASSWORD': '#Jmascis72',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
