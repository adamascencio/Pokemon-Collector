from django.shortcuts import render
from .models import Pokemon

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  p = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': p})
