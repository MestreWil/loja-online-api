from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pedidos_produtos
from .serializers import PedidoProdutoSerializer

import json

@api_view(['GET'])
def get_pedido_produto(request):
    if request.method == 'GET':
      pedido_produto = Pedidos_produtos.objects.all()

      serializers = PedidoProdutoSerializer(pedido_produto, many=True)
      return Response(serializers.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET"])
# def clientes_por_id(request, pk):

#     try:
#         cliente_id = Clientes.objects.get(pk=pk)
#         serializer = ClientesSerializer(cliente_id)
#         return Response(serializer.data)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def post_pedido_produto(request):
  if request.method == 'POST':
    novo_pedido_produto = request.data
    serializer = PedidoProdutoSerializer(data=novo_pedido_produto)
    
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['PUT'])
def atualizar_pedido_produto(request):
  id_pedido_produto = request.data['id']
    
  try:
    atualizar_pedido_produto = PedidoProdutoSerializer.objects.get(pk=id_pedido_produto)
    
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  print(request.data)
    
  serializer = PedidoProdutoSerializer(atualizar_pedido_produto, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_pedido_produto(request, pk):
  try:
    deletar_pedido_produto = Pedidos_produtos.objects.get(pk=pk)
    deletar_pedido_produto.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
