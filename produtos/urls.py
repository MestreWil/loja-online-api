from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_produtos, name='get_all_clientes'),
    path('dados/<int:pk>', views.produtos_por_id),
    path('novo_produto', views.post_produtos),
    path('atualizar_produto', views.atualizar_produtos),
    path('deletar_produto/<int:pk>', views.excluir_produtos),      
]