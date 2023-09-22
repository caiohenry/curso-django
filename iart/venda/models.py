from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from cliente.models import Cliente

class Venda(models.Model):
    
    valor_venda = models.DecimalField(_("Valor da Venda"), max_digits=8, decimal_places=2)
    data_venda = models.DateTimeField(_("Data da Venda"), blank=True, default=timezone.now)
    
    cliente = models.ForeignKey(Cliente, related_name="cliente_venda", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"cliente {self.cliente.nome_cliente} no valor {self.valor_venda}"
    
    class Meta:
        db_table = "venda"
        app_label = "venda"
    
    