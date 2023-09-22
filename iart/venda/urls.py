from django.urls import path
from .views import *


urlpatterns = [
    path('', VendaListagem.as_view()),
    path('cadastrar/', VendaCadastrar.as_view()),
    path("deletar/<int:pk>/", VendaDeletar.as_view()),
    
    path("filtrar-cliente/<int:id_cliente>/", VendaFiltragemCliente.as_view())
]