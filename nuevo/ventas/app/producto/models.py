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




















