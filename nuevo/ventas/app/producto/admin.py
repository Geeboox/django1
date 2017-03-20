from django.contrib import admin
from app.producto.models import producto,stock,precios

# Register your models here.

admin.site.register(producto)
admin.site.register(stock)
admin.site.register(precios)
