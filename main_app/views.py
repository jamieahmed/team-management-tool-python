from django.shortcuts import render
from django.http import HttpResponse

from main_app.models import Team

from .models import Team


# Add the Team class & list and view function below the imports
class team:  # Note that parens are optional if not inheriting from another class
  def __init__(self, team, purpose, description, code):
    self.team = team
    self.purpose = purpose
    self.description = description
    self.code = code

teams = [
  team('Lolo', 'tabby', 'Kinda rude.', 3),
  team('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  team('Fancy', 'bombay', 'Happy fluff ball.', 4),
  team('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


# Define the home view
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def teams_index(request):
  teams = Team.objects.all()
  return render(request, 'teams/index.html', { 'teams': teams })

def teams_detail(request, team_id):
  teams = Team.objects.get(id=team_id)
  return render(request, 'teams/detail.html', { 'teams': teams })