from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
  path('pokemon/<int:pokemon_id>/add_item/', views.add_item, name='add_item'),
  path('moves/', views.MoveList.as_view(), name='moves_index'),
  path('moves/<int:pk>/', views.MoveDetail.as_view(), name='moves_detail'),
  path('moves/create/', views.MoveCreate.as_view(), name='moves_create'),
  path('moves/<int:pk>/update/', views.MoveUpdate.as_view(), name='moves_update'),
]