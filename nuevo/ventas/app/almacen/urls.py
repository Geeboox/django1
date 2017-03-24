from django.conf.urls import url,include
from app.almacen.views import index,almacen_view,almacen_list,almacen_edit,almacen_delete


#Ingresamos los urls.

urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^nuevo$',almacen_view,name='almacen_crear'),
	url(r'^listar$',almacen_list,name='almacen_listar'),
	url(r'^editar/(?P<id_almacen>\d+)/$',almacen_edit,name='almacen_editar'),
	url(r'^eliminar/(?P<id_almacen>\d+)/$',almacen_delete,name='almacen_eliminar'),
]

