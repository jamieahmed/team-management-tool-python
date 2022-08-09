from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('teams/', views.teams_index, name='teams_index'),
  path('teams/<int:team_id>/', views.teams_detail, name='teams_detail'),
]