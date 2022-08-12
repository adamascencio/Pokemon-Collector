from django.db import models
from django.urls import reverse

ITEMS = (
  ('PT', 'Potion'),
  ('SP', 'Super Potion'),
  ('HP', 'Hyper Potion'),
  ('RC', 'Rare Candy'),
  ('RV', 'Revive'),
)

# Create your models here.

class Move(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  damage = models.IntegerField()

  def __str__(self):
    return f'{self.name} - a {self.type} type move with {self.damage} damage points'

  def get_absolute_url(self):
    return reverse('moves_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  super_effective = models.TextField(max_length=250)
  weak_against = models.TextField(max_length=250)
  moves = models.ManyToManyField(Move)

  def __str__(self):
      return f'{self.name} - a {self.type} type pokemon'

  def get_absolute_url(self):
      return reverse('detail', kwargs={'pokemon_id': self.id})

  def at_max_moves(self):
    return self.moves.count() >= 4


class Item(models.Model):
  date = models.DateField()
  item = models.CharField(
      'Item Given',
      max_length=2,
      choices=ITEMS,
  )
  # Create a pokemon_id foreign key
  pokemon = models.ForeignKey(
    Pokemon, 
    on_delete=models.CASCADE
    )

  def __str__(self):
      return f'{self.get_item_display()} on {self.date}'
  
  class Meta:
    ordering = ['-date']
