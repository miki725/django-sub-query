# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.contrib.gis.db.models.sql.compiler import *  # noqa


class SubQueryGeoSQLCompiler(GeoSQLCompiler):
    def __init__(self, *args, **kwargs):
        super(SubQueryGeoSQLCompiler, self).__init__(*args, **kwargs)
        self.is_subquery = False

    def get_ordering(self):
        if hasattr(self, '_get_ordering'):
            values = self._get_ordering
        else:
            values = self._get_ordering = super(SubQueryGeoSQLCompiler, self).get_ordering()

        ordering, o_params, ordering_group_by = values

        if self.is_subquery:
            ordering = []

        return ordering, o_params, ordering_group_by

    def pre_sql_setup(self):
        if hasattr(self, '_pre_sql_setup'):
            return self._pre_sql_setup

        self._pre_sql_setup = super(SubQueryGeoSQLCompiler, self).pre_sql_setup()
        return self._pre_sql_setup

    def get_columns(self, with_aliases=False):
        if hasattr(self, '_get_columns'):
            return self._get_columns

        self._get_columns = super(SubQueryGeoSQLCompiler, self).get_columns(with_aliases)
        return self._get_columns

    def as_sql(self, with_limits=True, with_col_aliases=False):
        # these calls are required in order to get ordering columns
        self.pre_sql_setup()
        self.get_columns(with_col_aliases)

        ordering, o_params, ordering_group_by = self.get_ordering()
        distinct_fields = self.get_distinct()

        self.is_subquery = False

        if self.query.distinct and ordering:
            distinct_ordering_pairs = list(zip(distinct_fields, ordering))

            if not all(map(lambda i: i[1].startswith(i[0]), distinct_ordering_pairs)):
                self.is_subquery = True

        sql, params = super(SubQueryGeoSQLCompiler, self).as_sql(
            with_limits=with_limits, with_col_aliases=with_col_aliases
        )

        if self.is_subquery:
            sql = ' '.join(filter(None, [
                'SELECT',
                '*',
                'FROM (',
                '{}'.format(sql),
                ')',
                '"{}"'.format(self.query.model._meta.db_table),
                'ORDER BY',
                '{}'.format(', '.join(ordering)),
            ] + o_params))
            self.is_subquery = False

        return sql, params
