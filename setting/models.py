from django.db import models

class Belong(models.Model):
    user_id = models.IntegerField(default=-1)
    group_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user_id) + '-->' + self.group_name

# Create your models here.
