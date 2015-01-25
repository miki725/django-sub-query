# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.contrib.gis.db.backends.postgis.base import DatabaseWrapper as _DatabaseWrapper
from django.db.backends.creation import NO_DB_ALIAS

from .operations import SubQueryPostGISOperations


class DatabaseWrapper(_DatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        if kwargs.get('alias', '') != NO_DB_ALIAS:
            self.ops = SubQueryPostGISOperations(self)
