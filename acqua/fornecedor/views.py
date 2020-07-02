from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from acqua.fornecedor.forms import FornecedorForm
from acqua.fornecedor.models import Fornecedor


def fornecedor_list(request):
    template_name = 'fornecedor_list.html'
    objects = Fornecedor.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(razao__icontains=search)
    context = {'objects_list': objects}
    return render(request, template_name, context)


class FornecedorList(ListView):
    template_name = 'fornecedor_list.html'
    model = Fornecedor
    paginate_by = 10


def fornecedor_detail(request, pk):
    template_name = 'fornecedor_detail.html'
    obj = Fornecedor.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def fornecedor_add(request):
    template_name = 'fornecedor_form.html'
    return render(request, template_name)


class FornecedorCreate(CreateView):
    model = Fornecedor
    template_name = 'fornecedor_form.html'
    form_class = FornecedorForm


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    template_name = 'fornecedor_form.html'
    form_class = FornecedorForm