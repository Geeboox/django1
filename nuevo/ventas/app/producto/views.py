from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.producto.forms import productoForm
from app.producto.models import producto


# Create your views here.

def index(request):
	return render(request,'producto/index.html')


def producto_view(request):

	if request.method == 'POST':
		form = productoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('producto:producto_listar')
	else:
		form = productoForm()
	        return render(request,'producto/producto_form.html',{'form':form})

def producto_list(request):
	p = producto.objects.all()
	contexto = {'producto':p}
	return render(request, 'producto/producto_list.html',contexto)


def producto_edit(request,id_producto):

	p2 = producto.objects.get(id=id_producto)

	if request.method == 'GET':
		form = productoForm(instance=p2)
	else:
		form=productoForm(instance=p2)
		if form.is_valid():
			form.save()
		return redirect('producto:producto_listar')

  	return render(request,'producto/producto_form.html',{'form':form})
	
def producto_delete(request,id_producto):
	
	p3 =producto.objects.get(id=id_producto)

	if request.method == 'POST':
		p3.delete()
		return redirect('producto:producto_listar')
	return render(request,'producto/producto_delete.html',{'producto':p3})
