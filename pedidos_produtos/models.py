from django.db import models
from pedidos.models import Pedido
from produtos.models import Produtos


class Pedidos_produtos(models.Model):
  pedido_int = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido_id')
  produto_int = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name='produto_id')
  preco = models.FloatField()
  quantidade = models.FloatField()
  
  
  def __str__(self):
    return f'Pedido_id: {self.pedido_int.id} | Produto: {self.produto_int.nome} | Preco: {self.preco} | Quantidade: {self.quantidade}'
