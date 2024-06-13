from django.db import models
from categorias.models import Categorias


class Produtos(models.Model):
  nome = models.CharField(max_length=100, unique=True)
  preco = models.FloatField()
  quantidade = models.FloatField()
  categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='categorias')
  
  def __str__(self):
    return f'Nome: {self.nome} | Preco: {self.preco} | Quantidade: {self.quantidade} | Categoria {self.categoria}' 
