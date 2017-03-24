from django.contrib import admin
from app.producto.models import producto,stock,precio

# Register your models here.

admin.site.register(producto)
admin.site.register(stock)
admin.site.register(precio)
