from django.urls import path
from .views import *


urlpatterns = [
    path('', ClienteListagem.as_view()),
    path('cadastrar/', ClienteCadastrar.as_view()),
    path("deletar/<int:pk>/", ClienteDeletar.as_view())
]