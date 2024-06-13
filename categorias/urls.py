from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_categorias, name='get_all_categorias'),
    path('dados/', views.categorias_manager),
    path('nova_categoria/', views.post_categoria),
    path('atualizar_categoria/', views.editar_categoria),
    path('deletar_categoria/<int:pk>', views.apagar_categoria),
] 