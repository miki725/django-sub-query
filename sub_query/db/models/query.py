# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.contrib.gis.db.models.query import GeoQuerySet

from .sql.query import SubQueryGeoQuery


class SubQueryGeoQuerySet(GeoQuerySet):
    def __init__(self, model=None, query=None, using=None, hints=None):
        super(SubQueryGeoQuerySet, self).__init__(
            model=model, query=query, using=using, hints=hints
        )
        self.query = query or SubQueryGeoQuery(self.model)
