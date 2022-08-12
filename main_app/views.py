from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Team
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view
class Home(LoginView):
  template_name = 'home.html'


def about(request):
  return render(request, 'about.html')

@login_required
def teams_index(request):
  teams = Team.objects.filter(user=request.user)
  return render(request, 'teams/index.html', { 'teams': teams })

def team_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  return render(request, 'teams/detail.html', { 'team': team })


class TeamCreate(LoginRequiredMixin,CreateView):
  model = Team
  fields = '__all__'
  success_url = '/teams/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TeamUpdate(LoginRequiredMixin,UpdateView):
  model = Team
  fields = ['team', 'purpose', 'description', 'code']

class TeamDelete(LoginRequiredMixin,DeleteView):
  model = Team
  success_url = '/teams/'



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('teams_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
 