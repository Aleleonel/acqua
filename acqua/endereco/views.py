from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from acqua.endereco.forms import EnderecoForm
from acqua.endereco.models import Endereco


def endereco_list(request):
    template_name = 'endereco_list.html'
    objects = Endereco.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(rua__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class EnderecoList(ListView):
    template_name = 'endereco_list.html'
    model = Endereco
    paginate_by = 10


def endereco_detail(request, pk):
    template_name = 'endereco_detail.html'
    obj = Endereco.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def endereco_add(request):
    template_name = 'endereco_form.html'
    return render(request, template_name)


class EnderecoCreate(CreateView):
    model = Endereco
    template_name = 'endereco_form.html'
    form_class = EnderecoForm


class EnderecoUpdate(UpdateView):
    model = Endereco
    template_name = 'endereco_form.html'
    form_class = EnderecoForm