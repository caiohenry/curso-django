from django.db import models
from django.utils.translation import gettext_lazy as _
from venda.models import Venda
from produto.models import Produto


class ProdutoVenda(models.Model):
    
    quantidade_produto_venda = models.IntegerField(_("Quantidade Produto"))
    
    venda = models.ForeignKey(Venda, related_name="venda_produto_venda", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name="produto_produto_venda", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.venda.cliente.nome_cliente
    class Meta:
        app_label = "produto_venda"
        db_table = "produto_venda"
    
