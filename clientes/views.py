from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Clientes
from .serializers import ClientesSerializer

import json

@api_view(['GET'])
def get_clientes(request):
  if request.method == 'GET':
    clientes = Clientes.objects.all()
    
    serializers = ClientesSerializer(clientes, many=True)
    return Response(serializers.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def clientes_por_id(request, pk):
    
    try:
      cliente_id = Clientes.objects.get(pk=pk)
      serializer = ClientesSerializer(cliente_id)
      return Response(serializer.data)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def post_cliente(request):
  if request.method == 'POST':
    novo_cliente = request.data
    serializer = ClientesSerializer(data=novo_cliente)
    
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
  
@api_view(['PUT'])
def atualizar_cliente(request):
  id_cliente = request.data['id']
    
  try:
    atualizar_cliente = Clientes.objects.get(pk=id_cliente)
    
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  print(request.data)
    
  serializer = ClientesSerializer(atualizar_cliente, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_cliente(request, pk):
  try:
    deletar_cliente = Clientes.objects.get(pk=pk)
    deletar_cliente.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)