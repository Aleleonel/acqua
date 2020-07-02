from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from acqua.cliente.forms import ClienteForm
from acqua.cliente.models import Cliente


def cliente_list(request):
    template_name = 'cliente_list.html'
    objects = Cliente.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class ClienteList(ListView):
    template_name = 'cliente_list.html'
    model = Cliente
    paginate_by = 10


def cliente_detail(request, pk):
    template_name = 'cliente_detail.html'
    obj = Cliente.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def cliente_add(request):
    template_name = 'cliente_form.html'
    return render(request, template_name)


class ClienteCreate(CreateView):
   model = Cliente
   template_name = 'cliente_form.html'
   form_class = ClienteForm


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm

