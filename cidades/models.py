from django.db import models

class Cidades(models.Model):
  nome = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return f'Cidade: {self.nome}'
