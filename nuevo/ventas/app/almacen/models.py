from __future__ import unicode_literals

from django.db import models

# Create your models here.
class almacen (models.Model):
	nombre = models.TextField()
	direccion = models.TextField()


