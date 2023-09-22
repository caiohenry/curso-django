from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Produto
        
        fields = "__all__"


class ProdutoListarSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Produto
        
        fields = ["id", "nome_produto"]