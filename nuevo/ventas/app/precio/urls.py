from django.conf.urls import url, include 
from django.contrib import admin
admin.autodiscover()
from app.precio.views import precio_list,precio_view,precio_edit,precio_delete




urlpatterns = [
	
	url(r'^nuevo_precio$',precio_view,name='precio_crear'),
	url(r'^listar_precio$',precio_list,name='precio_listar'),
	url(r'^editar_precio/(?P<id_precio>\d+)/$',precio_edit,name='precio_editar'),
	url(r'^eliminar_precio/(?P<id_precio>\d+)/$',precio_delete,name='precio_eliminar'),


]


