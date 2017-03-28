from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.almacen.forms import almacenForm
from app.almacen.models import almacen

# Create your views here.

def index(request):
	return render(request, 'almacen/index.html')

def almacen_view (request):
	
	if request.method == 'POST':
		form=almacenForm(request.POST)
			
		if form.is_valid():
			   form.save()
		return redirect('almacen:almacen_listar')
			
	else:
		form = almacenForm()
	return render(request,'almacen/almacen_form.html', {'form':form})

def almacen_list(request):
	a = almacen.objects.all().order_by('id')
	contexto = {'almacen':a}
	return render(request,'almacen/almacen_list.html',contexto)

def almacen_edit(request,id_almacen):
	a = almacen.objects.get(id=id_almacen)
	if request.method == 'GET':
		form = almacenForm(instance=a)
	else:
		form = almacenForm(request.POST,instance = a)
		if form.is_valid():
			form.save()
		return redirect('almacen:almacen_listar')
	return render(request,'almacen/almacen_form.html',{'form':form})

def almacen_delete(request,id_almacen):
	a = almacen.objects.get(id=id_almacen)
	if request.method == 'POST':
		a.delete()
		return redirect('almacen:almacen_listar')
	return render(request,'almacen/almacen_delete.html',{'almacen':a})
