from app.precio.models import precio
from django import forms
from .models import precio


class precioForm(forms.ModelForm):
	
	
	producto= forms.Select()
	ppack = forms.DecimalField(label='Precio Pack',max_digits=5,decimal_places=2)                 
	costo = forms.DecimalField(max_digits=5,decimal_places=2)
	mayorista = forms.DecimalField(max_digits=5,decimal_places=2)                 
	minorista = forms.DecimalField(max_digits=5,decimal_places=2)                 
	agencia = forms.DecimalField(max_digits=5,decimal_places=2)                 
	lista = forms.DecimalField(max_digits=5,decimal_places=2)                 



	class Meta:
	
		model = precio

		fields = ('producto','ppack','costo','mayorista','minorista','agencia','lista',)

