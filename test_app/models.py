# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from sub_query.db.models import SubQueryGeoQuerySet
from django.contrib.gis.db import models


class DistinctSortExample(models.Model):
    """
    Example model which where queries need to made where
    distinct and sort columns do not match.
    """
    distinct = models.CharField(max_length=32)
    sort = models.CharField(max_length=32)

    objects = SubQueryGeoQuerySet.as_manager()
