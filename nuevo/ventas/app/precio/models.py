from __future__ import unicode_literals

from django.db import models
from app.producto.models import producto

# Create your models here.


class precio(models.Model):          
	
	ppack = models.DecimalField(max_digits=5,decimal_places=2)         
	costo = models.DecimalField(max_digits=5,decimal_places=2)         
	mayorista = models.DecimalField(max_digits=5,decimal_places=2)         
	minorista = models.DecimalField(max_digits=5,decimal_places=2)         
	agencia = models.DecimalField(max_digits=5,decimal_places=2)         
	lista = models.DecimalField(max_digits=5,decimal_places=2)         
	pro_id = models.ForeignKey(producto,null=True,blank=True,on_delete=models.CASCADE)
