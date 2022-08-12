from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('teams/', views.teams_index, name='teams_index'),
  path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
  path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
  path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
  path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]