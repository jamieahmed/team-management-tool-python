from turtle import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Team(models.Model):
  team = models.CharField(max_length=100)
  purpose = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  code = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self): 
    return self.team
      
  def get_absolute_url(self):
    return reverse('team_detail', kwargs={'team_id': self.id})





  