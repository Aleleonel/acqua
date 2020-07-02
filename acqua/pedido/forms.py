from django import forms

from acqua.pedido.models import Pedido, PedidoItens
from acqua.produto.models import Produto


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoItensSaidaForm(forms.ModelForm):
    class Meta:
        model = PedidoItens
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoItensSaidaForm, self).__init__(*args, **kwargs)
        # Retorna somente produto com estoque maior que zero

        self.fields['produto'].queryset = Produto.objects.filter(estoque__gt=0)