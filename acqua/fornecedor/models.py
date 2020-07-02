from django.db import models
from acqua.endereco.models import Endereco


class Fornecedor(models.Model):
    TIPO_CHOICES = (
        ("Beb", "Bedidas"),
        ("Cer", "Cervejas"),
        ("Ali", "Alimentos"),
        ("Ute", "Utensílios")
    )

    razao = models.CharField(max_length=100, null=False, blank=False)
    fantasia = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=9)
    insc_est = models.CharField(max_length=9)
    dt_cadastro = models.DateField(auto_created=True)
    email = models.EmailField(null=False, blank=False)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
