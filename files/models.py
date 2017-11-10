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
    def __str__(self):
        return (str(self.id) + ' is ' +self.name)

class StFile(models.Model):
    owner= models.IntegerField(default = -1)
    path = models.CharField(max_length = 200) 
    name = models.CharField(max_length = 100)
    isDir= models.BooleanField(default = True)
    url  = models.CharField(max_length = 200)
    modifyDate = models.DateTimeField()
    createDate = models.DateTimeField()
    size = models.FloatField()
    def __str__(self):
        return (str(self.owner) + '\'s. ' + str(self.id) + ' is ' + self.path + self.name)
    

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StFile
        fields = ('id', 'owner', 'path','name','isDir','url','modifyDate','createDate','size')


