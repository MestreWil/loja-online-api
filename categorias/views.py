from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Categorias
from .serializers import CategoriasSerializer

import json

@api_view(['GET'])
def get_categorias(request):
  if request.method == 'GET':
    categorias = Categorias.objects.all()
    
    serializers = CategoriasSerializer(categorias, many=True)
    return Response(serializers.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def categorias_manager(request):
  
  if request.method == 'GET':
    
    try:
      
      if request.GET['categoria']:
        
        categoria_nome = request.GET['categoria']
        
        try:
          
          categoria = Categorias.objects.get(nome=categoria_nome)
        
        except:
          return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriasSerializer(cidade)
        return Response(serializer.data)
      
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_categoria(request):
  
  if request.method == 'POST':
    nova_categoria = request.data
    
    serializer = CategoriasSerializer(data=nova_categoria)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def editar_categoria(request):
  
  if request.method == 'PUT':
    id_categoria = request.data['id']
    
    try:
      atualizar_categorias = Categorias.objects.get(pk=id_categoria)
    
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    print(request.data)
    
    serializer = CategoriasSerializer(atualizar_categorias, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def apagar_categoria(request, pk):
    try:
      deletar_categoria = Categorias.objects.get(pk=pk)
      deletar_categoria.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)