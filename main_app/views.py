from django.shortcuts import render
from django.http import HttpResponse




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

# Add new view
def teams_index(request):
  return render(request, 'teams/index.html', { 'teams': teams })

  