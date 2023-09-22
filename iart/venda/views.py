from rest_framework import generics, status, response
from .models import Venda
from .serializers import VendaSerializer, VendaListarSerializer
from produto_venda.serializers import ProdutoVendaSerializer


class VendaListagem(generics.ListAPIView):
    
    queryset = Venda.objects.all()
    serializer_class = VendaListarSerializer

    def get(self, request):

        venda = self.queryset.all()
        Venda_serializer = self.serializer_class(venda, many=True)
        
        return response.Response(data = Venda_serializer.data, status = status.HTTP_200_OK)


class VendaCadastrar(generics.CreateAPIView):
    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
    def post(self, request):
        
        venda_serializer = self.serializer_class(data = request.data)
        
        if venda_serializer.is_valid():
            
            venda = venda_serializer.save()
            
            print(venda.valor_venda)
            
            itens = request.data.get("itens")
            
            for produto in itens:
                
                produto_serializer = ProdutoVendaSerializer(data = {
                    "produto": produto, 
                    "venda": venda.pk, 
                    "quantidade_produto_venda": 2})
                
                if produto_serializer.is_valid():
                    
                    produto_serializer.save()
                
                else:
                    
                    venda.delete()
                    
                    return response.Response(data = produto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
            return response.Response(data = venda_serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            
            return response.Response(data = venda_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            

class VendaDeletar(generics.RetrieveDestroyAPIView):
    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
    def delete(self, request, pk):
        
        venda = self.queryset.get(pk = pk)
        
        venda.delete()
        
        return response.Response(data = {}, status = status.HTTP_204_NO_CONTENT)
        

class VendaFiltragemCliente(generics.ListAPIView):
    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
    def get(self, request, id_cliente):
        
        venda = self.queryset.filter(cliente = id_cliente)
        
        venda_serializer = self.serializer_class(venda, many=True)
        
        return response.Response(data = venda_serializer.data, status= status.HTTP_200_OK)