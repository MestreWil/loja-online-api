from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_pedidos, name='get_all_pedidos'),
    path('dados/<int:pk>', views.pedido_por_id),
    path('novo_pedido', views.post_pedido),
    path('atualizar_pedido', views.atualizar_pedido),
    path('deletar_pedido/<int:pk>', views.excluir_pedido),      
]