from django.db import models

class Categorias(models.Model):
  nome = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return f'Categoria: {self.nome}'