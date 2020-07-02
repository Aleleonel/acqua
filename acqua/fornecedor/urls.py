from django.urls import path
from acqua.fornecedor import views as v

app_name = 'fornecedor'

urlpatterns = [
    path('', v.FornecedorList.as_view(), name='fornecedor_list'),
    path('<int:pk>/', v.fornecedor_detail, name='fornecedor_detail'),
    path('add/', v.FornecedorCreate.as_view(), name='fornecedor_add'),
    path('<int:pk>/edit/', v.FornecedorUpdate.as_view(), name='fornecedor_edit'),
    ]