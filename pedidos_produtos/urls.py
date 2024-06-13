from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_pedido_produto, name='get_all_pedidos_produto'),
    path('novo_pedido', views.post_pedido_produto),
    path('atualizar_pedido', views.atualizar_pedido_produto),
    path('deletar_pedido/<int:pk>', views.excluir_pedido_produto),      
]