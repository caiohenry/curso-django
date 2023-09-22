from django.db import models
from django.utils.translation import gettext_lazy as _

class Produto(models.Model):
    
    preco_produto = models.DecimalField(_("Preço do Produto"), max_digits=8, decimal_places=2)
    nome_produto = models.CharField(_("Nome Produto"), max_length=255)
    
    
    def __str__(self):
        return self.nome_produto

    class Meta:
        app_label = "produto"
        db_table = "produto"
    