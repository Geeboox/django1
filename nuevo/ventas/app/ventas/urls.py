from django.conf.urls import url, include

from app.ventas.views import index


urlpatterns = [
	url(r'^$',index,name='index'),
]
