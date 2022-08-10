from django.db import models

from django.urls import reverse

class Team(models.Model):
  team = models.CharField(max_length=100)
  purpose = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  code = models.IntegerField()

def __str__(self):
    return self.team
      
def get_absolute_url(self):
    return reverse('teams_detail', kwargs={'teams_id': self.id})
