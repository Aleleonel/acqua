from django.db import models
from django.urls import reverse_lazy

from acqua.estoque.models import Estoque
from acqua.produto.models import Produto
from acqua.pedido.manager import PedidoSaidaManager

MOVIMENTO = (
    ('s', 'saida'),
)


class Pedido(models.Model):
    STATUS_CHOICES = (
        ("E", "Efetivado"),
        ("O", "Orçamento"),
        ("C", "Cancelado"),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    cliente = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    data_pedido = models.DateField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto)
    valor = models.FloatField(blank=False, null=False)
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, default='s', blank=True)

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse_lazy('pedido:pedido_detail', kwargs={'pk': self.pk})


class PedidoSaida(Pedido):

    objects = PedidoSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'pedido saida'
        verbose_name_plural = 'pedido saida'


class PedidoItens(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoque'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk', )

    def __str__(self):
        return '{}, {}, {}'.format(self.pk, self.estoque.pk, self.produto)