from rest_framework import generics, status, response
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteListagem(generics.ListAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request):

        clientes = self.queryset.all()
        cliente_serializer = self.serializer_class(clientes, many=True)
        
        return response.Response(data = cliente_serializer.data, status = status.HTTP_200_OK)


class ClienteCadastrar(generics.CreateAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def post(self, request):
        
        cliente_serializer = self.serializer_class(data = request.data)
        
        if cliente_serializer.is_valid():
            
            cliente_serializer.save()
            
            return response.Response(data = cliente_serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            
            return response.Response(data = cliente_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            

class ClienteDeletar(generics.RetrieveDestroyAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def delete(self, request, pk):
        
        cliente = self.queryset.get(pk = pk)
        
        cliente.delete()
        
        return response.Response(data = {}, status = status.HTTP_204_NO_CONTENT)
        

class NomeFiltragem(generics.ListAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def get(self, request, nome):
        
        clientes = self.queryset.filter(nome_cliente = nome)
        cliente_serializer = self.serializer_class(clientes, many=True)
        
        return response.Response(data = cliente_serializer.data, status = status.HTTP_200_OK)