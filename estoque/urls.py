from django.urls import path, include
from .views import *


urlpatterns = [
    # Outras URLs do aplicativo
    path('', HomePageView, name='home'),

    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),

]