# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.contrib.gis.db.models.sql import GeoQuery


class SubQueryGeoQuery(GeoQuery):
    compiler = 'SubQueryGeoSQLCompiler'
