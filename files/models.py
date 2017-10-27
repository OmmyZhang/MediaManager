from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FileToTag(models.Model):
    file_id = models.IntegerField(default=0)
    tag_id = models.IntegerField(default=0)  # < 0 if a group 
    def __str__(self):
        return str(self.file_url) + '-->' + str(self.tag_id)

class StTag(models.Model):
    name = models.CharField(max_length = 100)
    isGroup = models.BooleanField(default = False)
    def __str__(self):
        return (str(self.id) + ' is ' +self.name)#.encode('utf-8')

class StFile(models.Model):
    owner= models.IntegerField(default = -1)
    path = models.CharField(max_length = 200) 
    name = models.CharField(max_length = 100)
    def __str__(self):
        return (str(self.owner) + '\'s. ' + str(self.id) + ' is ' + self.path + self.name)#.encode('utf-8')
    



