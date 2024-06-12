from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_cidades, name='get_all_cidades'),
    path('dados/', views.cidade_manager),
    path('nova_cidade/', views.post_cidade),
    path('atualizar_cidade/', views.editar_cidade),
    path('deletar_cidade/<int:pk>', views.apagar_cidade),
] 
