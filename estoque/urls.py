from django.urls import path, include
from .views import *


urlpatterns = [
    # Outras URLs do aplicativo
    path('', HomePageView, name='home'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
    path('listar-produtos/', produtos_cadastrados, name='produtos_cadastrados'),
    path('listar-produtos/delete/<int:pk>/', produto_delete, name='produto_delete'),
    path('produto/<int:produto_id>/editar/', editar_produto, name='editar_produto'),
    path('enderecar_produto/', enderecar_produto, name='enderecar_produto'),
    path('localizar_produto/', localizar_produto, name='localizar_produto'),

]