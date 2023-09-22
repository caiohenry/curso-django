from rest_framework import serializers
from .models import ProdutoVenda
from produto.serializers import ProdutoListarSerializer


class ProdutoVendaSerializer(serializers.ModelSerializer):
    
    produto = ProdutoListarSerializer(read_only = True, many=False)
    
    class Meta:
        
        model = ProdutoVenda
        
        fields = ["id", "quantidade_produto_venda", "produto"]
        
        extra_kwargs = {
            "produto": {"required": True}
        }