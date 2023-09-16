from django.db import models
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    
    nome_cliente = models.CharField(_("Nome do Cliente"), max_length=255)
    endereco_cliente = models.CharField(_("Endereço do Cliente"), max_length=255)
    email_cliente = models.EmailField(_("Email do Cliente"), max_length=255)
    telefone_cliente = models.CharField(_("Telefone do Cliente"), max_length=15)
    
    def __str__(self):
        return self.nome_cliente

    class Meta:
        app_label = "cliente"
        db_table = "cliente"
    

    