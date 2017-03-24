from django import forms

from app.producto.models import producto



class productoForm(forms.ModelForm):

	class Meta:
		model=producto

		fields= [
		'fecha',
		'linea',
		'codigo',
		'marca',
		'descripcion',
		'n_comercial',
		'imagen',
		]
		labels = {
		'fecha':'Fecha',
                 'linea':'Linea',
                 'codigo':'Codigo',
                 'marca':'Marca',
                'descripcion':'Descripcion',
                 'n_comercial':'Nombre Comercial',
                 'imagen':'Imagen',
		}
		widgets = {
				'fecha':forms.DateInput(attrs={'class':'form-control'}),
                 'linea':forms.TextInput(attrs={'class':'form-control'}),
                 'codigo':forms.TextInput(attrs={'class':'form-control'}),
                 'marca':forms.TextInput(attrs={'class':'form-control'}),
                'descripcion':forms.TextInput(attrs={'class':'form-control'}),
                 'n_comercial':forms.TextInput(attrs={'class':'form-control'}),
                 'imagen':forms.TextInput(attrs={'class':'form-control'}),
		}







			












			
		
	













