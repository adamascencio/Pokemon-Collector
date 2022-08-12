from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Move, Pokemon
from .forms import ItemForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  p = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': p})

def pokemon_detail(request, pokemon_id):
  p = Pokemon.objects.get(id=pokemon_id)
  # instantiate ItemForm to be rendered in the template
  item_form = ItemForm()
  return render(request, 'pokemon/detail.html', {'pokemon': p, 'item_form': item_form})

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['type', 'super_effective', 'weak_against']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

def add_item(request, pokemon_id):
  form = ItemForm(request.POST)
  if form.is_valid():
    new_item = form.save(commit=False)
    new_item.pokemon_id = pokemon_id
    new_item.save()
  return redirect('detail', pokemon_id=pokemon_id)

class MoveList(ListView):
  model = Move

class MoveDetail(DetailView):
  model = Move

class MoveCreate(CreateView):
  model = Move
  fields = '__all__'

class MoveUpdate(UpdateView):
  model = Move
  fields = '__all__'

class MoveDelete(DeleteView):
  model = Move
  success_url = '/moves/'