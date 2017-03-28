from django.conf.urls import url, include 
from app.stock.views import stock_view,stock_list,stock_edit,stock_delete


urlpatterns = [

	url(r'^nuevo_stock$',stock_view,name='stock_crear'),
	url(r'^listar_stock$',stock_list,name='stock_listar'),
	url(r'^editar_stock/(?P<id_stock>\d+)/$',stock_edit,name='stock_editar'),
	url(r'^eliminar_stock/(?P<id_stock>\d+)/$',stock_delete,name='stock_eliminar'),
]
