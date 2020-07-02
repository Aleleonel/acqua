from django.urls import path
from acqua.endereco import views as v

app_name = 'endereco'

urlpatterns = [
    path('', v.EnderecoList.as_view(), name='endereco_list'),
    path('<int:pk>/', v.endereco_detail, name='endereco_detail'),
    path('add/', v.EnderecoCreate.as_view(), name='endereco_add'),
    path('<int:pk>/edit/', v.EnderecoUpdate.as_view(), name='endereco_edit'),
]