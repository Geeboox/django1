from django import forms
from datetime import datetime
from app.producto.models import producto



class DateInput(forms.DateInput):     
	input_type = 'date'

class productoForm(forms.ModelForm):

	fecha = forms.DateField()
	linea = forms.CharField()
	codigo = forms.CharField()
	marca = forms.CharField()
	descripcion = forms.CharField()
	n_comercial = forms.CharField()
	imagen = forms.CharField()


	class Meta:
		model=producto

		fields= ['fecha','linea','codigo','marca','descripcion','n_comercial','imagen',]
		widgets = {             
		'fecha': DateInput()         
		}
