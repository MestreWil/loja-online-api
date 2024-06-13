from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidades/', include('cidades.urls'), name='cidades_urls'),
    path('clientes/', include('clientes.urls'), name='clientes_urls'),
    path('pedidos/', include('pedidos.urls'), name='pedidos_urls'),
    path('categorias/', include('categorias.urls'), name='categorias_urls'),
    path('produtos/', include('produtos.urls'), name='produtos_urls'),
    path('pedidos_produtos/', include('pedidos_produtos.urls'), name='pedidos_produtos_urls'),
]
