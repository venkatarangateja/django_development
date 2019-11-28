# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	name        = models.CharField(max_length=120)
	local       = models.CharField(max_length=120,null=True,blank=True)
	category    = models.CharField(max_length=120,null=True,blank=False)
	timestamp   = models.DateTimeField(auto_now_add=True)
	updated     = models.DateTimeField(auto_now=True)
