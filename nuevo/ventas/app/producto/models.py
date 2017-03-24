from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

 

# Create your models here.

class producto(models.Model):
	fecha = models.DateField()
	linea = models.TextField()
	codigo = models.TextField()
	marca = models.TextField()
	descripcion = models.TextField()
	n_comercial = models.TextField()
 	imagen = models.TextField()


class precio(models.Model):

	ppack = models.DecimalField(max_digits=5,decimal_places=2)
	costo = models.DecimalField(max_digits=5,decimal_places=2)
	mayorista = models.DecimalField(max_digits=5,decimal_places=2)
	minorista = models.DecimalField(max_digits=5,decimal_places=2)
	agencia = models.DecimalField(max_digits=5,decimal_places=2)
	lista = models.DecimalField(max_digits=5,decimal_places=2)
	id_pro = models.ForeignKey(producto)


class stock(models.Model):

	cantidad = models.IntegerField()
	u_medida = models.TextField()
	almacen = models.IntegerField()
	d_pro = models.ForeignKey(producto)

