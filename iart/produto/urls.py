from django.urls import path
from .views import *


urlpatterns = [
    path('', ProdutoListagem.as_view()),
    path('cadastrar/', ProdutoCadastrar.as_view()),
    path("deletar/<int:pk>/", ProdutoDeletar.as_view())
]