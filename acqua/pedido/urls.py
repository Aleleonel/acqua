from django.urls import path, include
from acqua.pedido import views as v

app_name = 'pedido'

entrada_patterns = [
    path('', v.PedidosListView.as_view(), name='pedido_list'),
    path('add/', v.PedidoCreate.as_view(), name='pedido_add'),

]

saida_patterns = [
    path('', v.PedidoSaidaList.as_view(), name='pedido_saida_list'),
    path('add/', v.pedido_saida_add, name='pedido_saida_add'),

]

urlpatterns = [

    path('<int:pk>/', v.pedidos_detail, name='pedido_detail'),
    path('<int:pk>/edit/', v.PedidoUpdate.as_view(), name='pedido_edit'),
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),



    ]
