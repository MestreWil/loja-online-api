from django.db import models
from clientes.models import Clientes

class Pedido(models.Model):
  horario = models.DateTimeField()
  endereco = models.CharField(max_length=200)
  cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='clientes')
  
  def __str__(self):
    return f'Cliente: {self.cliente.nome} | Endereço: {self.endereco}' 
