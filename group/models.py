from django.db import models

class Belong(models.Model):
    user_id = models.IntegerField(default=-1)
    group_id = models.IntegerField(default=-1)
    def __str__(self):
        return str(self.user_id) + '-->' + str(self.group_id)

# Create your models here.
