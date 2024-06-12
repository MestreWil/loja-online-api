from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_clientes, name='get_all_clientes'),
    path('dados/<int:pk>', views.clientes_por_id),
    path('novo_cliente', views.post_cliente),
    path('atualizar_cliente', views.atualizar_cliente),
    path('deletar_cliente/<int:pk>', views.excluir_cliente),      
]