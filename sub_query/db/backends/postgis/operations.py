# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from django.contrib.gis.db.backends.postgis.operations import PostGISOperations


class SubQueryPostGISOperations(PostGISOperations):
    compiler_module = 'sub_query.db.models.sql.compiler'
