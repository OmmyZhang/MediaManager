from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FileToGroup(models.Model):
    file_url = models.CharField(max_length=500)
    group_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.file_url) + '-->' + self.group_name



