from django.db import models
from app.almacen.models import almacen
from app.producto.models import producto


# Create your models here.

class stock(models.Model):

	cantidad = models.DecimalField(max_digits=5,decimal_places=2)
	u_medida = models.TextField()
	almacen = models.ForeignKey(almacen)
	producto = models.ForeignKey(producto)
