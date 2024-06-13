from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Produtos
from .serialiers import ProdutosSerializer

import json

@api_view(['GET'])
def get_produtos(request):
  if request.method == 'GET':
    produtos = Produtos.objects.all()
    
    serializers = ProdutosSerializer(produtos, many=True)
    return Response(serializers.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def produtos_por_id(request, pk):
    
    try:
      produtos_id = Produtos.objects.get(pk=pk)
      serializer = ProdutosSerializer(produtos_id)
      return Response(serializer.data)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def post_produtos(request):
  if request.method == 'POST':
    novo_produtos = request.data
    serializer = ProdutosSerializer(data=novo_produtos)
    
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
  
@api_view(['PUT'])
def atualizar_produtos(request):
  id_produto = request.data['id']
    
  try:
    atualizar_produtos = Produtos.objects.get(pk=id_produto)
    
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  print(request.data)
    
  serializer = ProdutosSerializer(atualizar_produtos, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_produtos(request, pk):
  try:
    deletar_produtos = Produtos.objects.get(pk=pk)
    deletar_produtos.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)