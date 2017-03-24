from django.conf.urls import url, include
from app.mascota.views import index
urlpatterns = [
url(r'^$', index),
]
