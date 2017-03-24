from django import forms

from app.almacen.models import almacen



class almacenForm(forms.ModelForm):

	class Meta:
		model = almacen
		fields=[ 
				'nombre',
				'direccion',
		]
		labels = {
				'nombre':'Nombre',
				'direccion':'Direccion',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),	
		}
