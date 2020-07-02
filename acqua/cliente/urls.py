
from django.urls import path
from acqua.cliente import views as v

app_name = 'cliente'

urlpatterns = [
    path('', v.ClienteList.as_view(), name='cliente_list'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('add/', v.ClienteCreate.as_view(), name='cliente_add'),
    path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
    ]