import code
from ssl import Purpose
from django.db import models


class Team(models.Model):
  team = models.CharField(max_length=100)
  Purpose = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  code = models.IntegerField()
  
def __str__(self):
    return self.team