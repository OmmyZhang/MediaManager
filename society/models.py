# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PeopleFollowPeople(models.Model):
	followee = models.IntegerField();
	follower = models.IntegerField();
	
class PeopleStarFile(models.Model):
	people = models.IntegerField();
	fileid = models.IntegerField();

class PeopleComment(models.Model):
	people = models.IntegerField();
	fileid = models.IntegerField();
	comment = models.CharField(max_length = 200);
	# This may not halal, I may try to deal with Chinese Character

# Create your models here.
