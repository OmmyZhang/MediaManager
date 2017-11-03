# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PeopleFollowPeople(models.Model):
	followee = models.IntegerField();
	follower = models.IntegerField();
	def __str__(self):
		return str(self.followee) + ' followed ' + str(self.follower)
	
class PeopleStarFile(models.Model):
	people = models.IntegerField();
	fileid = models.IntegerField();
	def __str__(self):
		return str(self.people) + ' stared ' + str(self.fileid)

class PeopleComment(models.Model):
	people = models.IntegerField();
	fileid = models.IntegerField();
	comment = models.CharField(max_length = 200);
	def __str__(self):
		return str(self.people) + '-->' + str(self.fileid) + '-->' + str(self.comment)
	# This may not halal, I may try to deal with Chinese Character

# Create your models here.
