from django import forms 
from app.stock.models import stock
from .models import stock



class stockForm(forms.ModelForm):

	producto = forms.Select()
	almacen = forms.Select()         
	u_medida = forms.CharField()
	cantidad = forms.DecimalField(max_digits=5,decimal_places=2)         

	class Meta:                  
		model = stock                  
	
		fields = ('producto','almacen','u_medida','cantidad',)
