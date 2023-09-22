from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Cliente
        
        fields = "__all__"
        

class ClienteListarVendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Cliente
        
        fields = ["id", "nome_cliente", "email_cliente"]
        