# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.db.backends.creation import NO_DB_ALIAS
from django.test import TestCase

from django.conf import settings
from sub_query.db.backends.postgis.base import DatabaseWrapper
from sub_query.db.backends.postgis.operations import SubQueryPostGISOperations


class TestDatabaseWrapper(TestCase):
    def test_init_opts(self):
        wrapper = DatabaseWrapper(settings.DATABASES['default'])

        self.assertIsInstance(wrapper.ops, SubQueryPostGISOperations)

    def test_init_opts_no_db(self):
        wrapper = DatabaseWrapper(
            settings.DATABASES['default'],
            alias=NO_DB_ALIAS,
        )

        self.assertNotIsInstance(wrapper, SubQueryPostGISOperations)
