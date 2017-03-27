from django import forms 
from app.precio.models import precio



class precioForm(forms.ModelForm):



	class Meta:


		model = precio

	
		fields = [
		'ppack',
		'costo',
		'mayorista',
		'minorista',
		'agencia',
		'lista',	
		'pro_id',
		]
		labels = {
		'ppack': ppack,
		'costo': costo,
		'mayorista': mayorista,
		'minorista': minorista,
		'agencia': agencia,
		'lista': lista,
		'pro_id': pro_id,
		}
		widgets = {
		'ppack':forms.DecimalField(max_digits=5,decimal_places=2),
		'costo':forms.DecimalField(max_digits=5,decimal_places=2),
		'mayorista':forms.DecimalField(max_digits=5,decimal_places=2),
		'minorista':forms.DecimalField(max_digits=5,decimal_places=2),
		'agencia':forms.DecimalField(max_digits=5,decimal_places=2),
		'lista':forms.DecimalField(max_digits=5,decimal_places=2),
		'pro_id':forms.Select(),
		}	


