from django.conf.urls import include , url



from app.precio.views import index_precio
from app.precio.views import precio_view
from app.precio.views import precio_list
from app.precio.views import precio_edit
from app.precio.views import precio_delete  



urlpatterns = [  
	url(r'^$',index_precio, name='index'),
	url(r'^nuevo_precio$',precio_view,name='precio_crear'),
	url(r'^listar_precio$',precio_list,name='precio_listar'),
	url(r'^editar_precio/(?P<id_precio>\d+)/$',precio_edit,name='precio_editar'),
	url(r'^eliminar_precio/(?P<id_precio>\d+)/$',precio_delete,name='precio_eliminar'), 
]
