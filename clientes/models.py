from django.db import models
from cidades.models import Cidades

class Clientes(models.Model):
  nome = models.CharField(max_length=100, unique=True)
  altura = models.FloatField(default=0.0)
  nascimento = models.DateField()
  cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, related_name='clientes')
  
  def __str__(self):
    return f'Nome: {self.nome} | Cidade: {self.cidade.nome}'  