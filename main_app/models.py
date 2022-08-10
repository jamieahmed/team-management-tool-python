from enum import unique
from turtle import mode
from django.db import models
from django.urls import reverse


# DAYS = (
#   ('M', 'Monday'),
#   ('T', 'Tuesday'),
#   ('T', 'Thursday'),
#   ('F', 'Friday'),
#   ('S', 'Saturday'),
#   ('S', 'Sunday'),
# )




class Team(models.Model):
  team = models.CharField(max_length=100)
  purpose = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  code = models.IntegerField()


def __str__(self):
    return self.team
      
def get_absolute_url(self):
    return reverse('teams_detail', kwargs={'teams_id': self.id})

# for employees info


class Employees(models.Model):
  date = models.DateField()
#   day = models.CharField(
#   	max_length=1,
# 		choices=DAYS,
# 		default=DAYS[0][0]
# )
  name = models.CharField(max_length=100)
  role = models.CharField(max_length=100)
  identification = models.IntegerField()
  attendance = models.BooleanField()
  note = models.CharField(max_length=100)
  # email = models.EmailField(max_length=254)
  # address = models.CharField(max_length=100)
  # website = models.URLField()
  # linkedin = models.URLField(_(""), max_length=200)
  # github = models.URLField(_(""), max_length=200)

team = models.ForeignKey(Team, on_delete=models.CASCADE)


# def __str__(self):
#     return f"{self.get_day_display()} on {self.date}"