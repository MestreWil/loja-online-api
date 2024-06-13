from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pedido
from .serializers import PedidoSerializer

import json

@api_view(['GET'])
def get_pedidos(request):
  if request.method == 'GET':
    pedido = Pedido.objects.all()
    
    serializers = PedidoSerializer(pedido, many=True)
    return Response(serializers.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pedido_por_id(request, pk):
    
    try:
      pedido_id = Pedido.objects.get(pk=pk)
      serializer = PedidoSerializer(pedido_id)
      return Response(serializer.data)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_pedido(request):
  if request.method == 'POST':
    novo_pedido = request.data
    serializer = PedidoSerializer(data=novo_pedido)
    
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['PUT'])
def atualizar_pedido(request):
  id_pedido = request.data['id']
    
  try:
    atualizar_pedido = Pedido.objects.get(pk=id_pedido)
    
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  print(request.data)
    
  serializer = PedidoSerializer(atualizar_pedido, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_pedido(request, pk):
  try:
    deletar_pedido = Pedido.objects.get(pk=pk)
    deletar_pedido.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
      