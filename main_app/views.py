from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>team-management-tool</h1>')