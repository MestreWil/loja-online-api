from rest_framework import serializers
from .models import Pedidos_produtos

class PedidoProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pedidos_produtos
    fields = '__all__'