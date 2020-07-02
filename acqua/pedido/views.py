from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views.generic import ListView, CreateView, UpdateView

from acqua.estoque.forms import EstoqueItensSaidaForm
from acqua.pedido.models import PedidoSaida
from acqua.pedido.forms import PedidoForm, PedidoItensSaidaForm
from acqua.pedido.models import Pedido


def pedido_list(request):
    template_name = 'pedido_list.html'
    objects = Pedido.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(pedido_icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class PedidosListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'


def pedidos_detail(request, pk):
    template_name = 'pedido_detail.html'
    obj = Pedido.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def pedido_add(request):
    template_name = 'pedido_form.html'
    return render(request, template_name)


def pedido_saida_add(request):
    form_inline = PedidoItensSaidaForm
    template_name = 'pedido_saida_form.html'
    movimento = 's'
    url = 'pedido:pedido_detail'
    context = pedido_add(request, form_inline, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


def pedido_saida_list(request):
    template_name = 'pedido_list.html'
    objects = PedidoSaida.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'Pedido Saída',
        'url_add': 'pedido:pedido_saida_add'
    }
    return render(request, template_name, context)


class PedidoSaidaList(ListView):
    model = PedidoSaida
    template_name = 'pedido_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PedidoSaidaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Pedido Saída'
        context['url_add'] = 'pedido:pedido_saida_add'
        return context


def pedido_saida_detail(request, pk):
    template_name = 'pedido_detail.html'
    obj = PedidoSaida.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'pedido:pedido_saida_list'
    }
    return render(request, template_name, context)



class PedidoCreate(CreateView):
    model = Pedido
    template_name = 'pedido_form.html'
    form_class = PedidoForm


class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = 'pedido_form.html'
    form_class = PedidoForm