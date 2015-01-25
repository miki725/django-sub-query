# -*- coding: utf-8 -*-
"""
Bare ``settings.py`` for running tests for url_filter
"""
from __future__ import print_function, unicode_literals


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'sub_query.db.backends.postgis',
        'NAME': 'sub_query_test',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    'django_extensions',
    'django_nose',
    'sub_query',
    'test_app',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

STATIC_URL = '/static/'
SECRET_KEY = 'foo'
