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
            values = super(SubQueryGeoSQLCompiler, self).get_ordering()

        ordering, o_params, ordering_group_by = values

        if self.is_subquery:
            ordering = []

        return ordering, o_params, ordering_group_by

    def get_columns(self, with_aliases=False):
        if hasattr(self, '_get_columns'):
            return self._get_columns

        return super(SubQueryGeoSQLCompiler, self).get_columns(with_aliases)

    def as_sql(self, with_limits=True, with_col_aliases=False):
        self.get_columns(with_col_aliases)
        ordering, o_params, ordering_group_by = self.get_ordering()
        distinct_fields = self.get_distinct()

        self.is_subquery = False

        if self.query.distinct and ordering:
            distinct_ordering_pars = zip(distinct_fields, ordering)

            if not all(map(lambda i: i[0] == i[1], distinct_ordering_pars)):
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
                ') result',
                'ORDER BY',
                '{}'.format(', '.join(ordering)),
            ] + o_params))
            self.is_subquery = False

        return sql, params
