from rest_framework import serializers
from .models import Venda
from cliente.serializers import ClienteListarVendaSerializer
from produto_venda.serializers import ProdutoVendaSerializer


class VendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Venda
        
        fields = "__all__"


class VendaListarSerializer(serializers.ModelSerializer):
    
    cliente = ClienteListarVendaSerializer(read_only = True, many=False)
    venda_produto_venda = ProdutoVendaSerializer(read_only = True, many=True)
    
    class Meta:
        
        model = Venda
        
        fields = ["id", "valor_venda", "data_venda", "cliente", "venda_produto_venda"]
        
        extra_kwags = {
            "cliente": {"required": True},
            "venda_produto_venda": {"required": True}
        }