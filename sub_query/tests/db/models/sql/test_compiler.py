# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import mock
from django.test import TestCase

from sub_query.db.models.sql.compiler import SubQueryGeoSQLCompiler
from test_app.models import DistinctSortExample


class TestSubQueryGeoSQLCompiler(TestCase):
    def test_init(self):
        qs = SubQueryGeoSQLCompiler(
            mock.sentinel.query,
            mock.sentinel.connection,
            mock.sentinel.using,
        )

        self.assertFalse(qs.is_subquery)

    def test_distinct_sort_query(self):
        qs = (
            DistinctSortExample.objects
            .all()
            .distinct('distinct')
            .order_by('sort')
        )
        query = qs.query.sql_with_params()[0]

        # make sure db does not blow up
        list(qs.all())

        self.assertTrue(query.startswith(
            'SELECT * FROM ('
        ))
        self.assertTrue(
            ') "{}" ORDER BY'.format(DistinctSortExample._meta.db_table) in query
        )

    def test_distinct_sort_query_same_columns(self):
        qs = (
            DistinctSortExample.objects
            .all()
            .distinct('sort')
            .order_by('sort')
        )
        query = qs.query.sql_with_params()[0]

        # make sure db does not blow up
        list(qs.all())

        self.assertFalse(query.startswith(
            'SELECT * FROM (',
        ))
        self.assertFalse(
            ') "{}" ORDER BY'.format(DistinctSortExample._meta.db_table) in query
        )

    def test_distinct_sort_query_count(self):
        query = []

        original_as_sql = SubQueryGeoSQLCompiler.as_sql
        with mock.patch.object(SubQueryGeoSQLCompiler, 'as_sql', autospec=True) as mock_as_sql:
            def as_sql(self, *args, **kwargs):
                sql, params = original_as_sql(self, *args, **kwargs)
                query.append(sql)
                return sql, params

            mock_as_sql.side_effect = as_sql

            (
                DistinctSortExample.objects
                .all()
                .distinct('distinct')
                .order_by('sort')
                .count()
            )

        self.assertGreater(len(query), 0)
        self.assertFalse(query[0].startswith(
            'SELECT * FROM (',
        ))
        self.assertFalse(
            ') "{}" ORDER BY'.format(DistinctSortExample._meta.db_table) in query[0]
        )
