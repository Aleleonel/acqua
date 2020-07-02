from django.db import models
from django.urls import reverse_lazy

from acqua.endereco.models import Endereco


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
            return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})