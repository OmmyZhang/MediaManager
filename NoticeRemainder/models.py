from django.db import models
class Notice(models.Model):
    userId = models.IntegerField()
    content = models.CharField(max_length = 200)
    time = models.FloatField() #marked by the time token
