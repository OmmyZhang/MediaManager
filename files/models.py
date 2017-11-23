from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

# Create your models here.

class FileToTag(models.Model):
    file_id = models.IntegerField(default=0)
    tag_id = models.IntegerField(default=0)
    def __str__(self):
        return str(self.file_id) + '-->' + str(self.tag_id)

class StTag(models.Model):
    name = models.CharField(max_length = 100)
    isGroup = models.BooleanField(default = False)
    color = models.CharField(max_length=20)
    def __str__(self):
        return str(self.id) + ' is ' +self.name + ' --> ' + self.color

class StFile(models.Model):
    ownerID = models.IntegerField(default = -1)
    path = models.CharField(max_length = 200) 
    name = models.CharField(max_length = 100)
    isDir= models.BooleanField(default = True)
    modifyDate = models.DateTimeField()
    createDate = models.DateTimeField()
    size = models.FloatField()
    def __str__(self):
        return (str(self.ownerID) + '\'s. ' + str(self.id) + ' is ' + self.path + self.name)
    

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StFile
        fields = ('id', 'ownerID', 'path','name','isDir','modifyDate','createDate','size')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = StTag
        fields = ('id', 'name', 'isGroup', 'color')


