from django.shortcuts import render

class Pokemon:
  def __init__(self, name, type, super_effective, weak_against):
    self.name = name
    self.type = type
    self.super_effective = super_effective
    self.weak_against = weak_against

pokemon = [
  Pokemon('Pikachu', 'Electric', ['Water', 'Flying'], ['Ground']),
  Pokemon('Squirtle', 'Water', ['Rock', 'Fire', 'Ground'], ['Grass', 'Electric']),
  Pokemon('Charmander', 'Fire', ['Grass', 'Ice', 'Bug', 'Steel'], ['Water', 'Ground', 'Rock']),
  Pokemon('Bulbasaur', 'Grass', ['Water', 'Ground', 'Rock'], ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})
