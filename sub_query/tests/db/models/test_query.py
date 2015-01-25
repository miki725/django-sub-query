# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import mock
from django.test import TestCase

from sub_query.db.models.query import SubQueryGeoQuerySet
from sub_query.db.models.sql.query import SubQueryGeoQuery


class TestSubQueryGeoQuerySet(TestCase):
    def test_init(self):
        qs = SubQueryGeoQuerySet()

        self.assertIsInstance(qs.query, SubQueryGeoQuery)

    def test_init_provided_query(self):
        qs = SubQueryGeoQuerySet(query=mock.sentinel.query)

        self.assertEqual(qs.query, mock.sentinel.query)
