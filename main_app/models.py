from django.db import models 
from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  super_effective = models.TextField(max_length=250)
  weak_against = models.TextField(max_length=250)
  
  def __repr__(self):
    return f'{self.name} - a {self.type} type pokemon'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pokemon_id': self.id})