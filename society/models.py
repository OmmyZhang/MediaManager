# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PeopleFollowPeople(models.Model):
	followee = models.IntegerField(default = 0)
	follower = models.IntegerField(default = 0)
	def __str__(self):
		return str(self.followee) + ' followed ' + str(self.follower)
	
class PeopleStarFile(models.Model):
	people = models.IntegerField(default = 0)
	fileid = models.CharField(max_length = 100)
	def __str__(self):
		return str(self.people) + ' stared ' + self.fileid

class PeopleComment(models.Model):
	commentid = models.IntegerField(default = 0)
	userid = models.BigIntegerField(default = 0)
	fileid = models.CharField(max_length = 100)
	date = models.CharField(max_length = 30)
	type = models.CharField(max_length = 20)
	star = models.BooleanField(default = False)
	score = models.IntegerField(default = 0)
	comment = models.CharField(max_length = 200)
	def __str__(self):
		return str(self.userid) + '-->' + self.fileid
	#  Much halal now

# Create your models here.
