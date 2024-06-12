from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cidades
from .serializers import CidadesSerializer

import json

@api_view(['GET'])
def get_cidades(request):
  if request.method == 'GET':
    cidades = Cidades.objects.all()
    
    serializers = CidadesSerializer(cidades, many=True)
    return Response(serializers.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cidade_manager(request):
  
  if request.method == 'GET':
    
    try:
      
      if request.GET['cidade']:
        
        cidade_nome = request.GET['cidade']
        
        try:
          
          cidade = Cidades.objects.get(nome=cidade_nome)
        
        except:
          return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CidadesSerializer(cidade)
        return Response(serializer.data)
      
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_cidade(request):
  
  if request.method == 'POST':
    nova_cidade = request.data
    
    serializer = CidadesSerializer(data=nova_cidade)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def editar_cidade(request):
  
  if request.method == 'PUT':
    id_cidade = request.data['id']
    
    try:
      atualizar_cidade = Cidades.objects.get(pk=id_cidade)
    
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    print(request.data)
    
    serializer = CidadesSerializer(atualizar_cidade, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def apagar_cidade(request, pk):
    try:
      deletar_cidade = Cidades.objects.get(pk=pk)
      deletar_cidade.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    