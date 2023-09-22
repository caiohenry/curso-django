from rest_framework import generics, status, response
from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoListagem(generics.ListAPIView):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request):

        produtos = self.queryset.all()
        produto_serializer = self.serializer_class(produtos, many=True)
        
        return response.Response(data = produto_serializer.data, status = status.HTTP_200_OK)


class ProdutoCadastrar(generics.CreateAPIView):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def post(self, request):
        
        produto_serializer = self.serializer_class(data = request.data)
        
        if produto_serializer.is_valid():
            
            produto_serializer.save()
            
            return response.Response(data = produto_serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            
            return response.Response(data = produto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            

class ProdutoDeletar(generics.RetrieveDestroyAPIView):
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def delete(self, request, pk):
        
        Produto = self.queryset.get(pk = pk)
        
        Produto.delete()
        
        return response.Response(data = {}, status = status.HTTP_204_NO_CONTENT)