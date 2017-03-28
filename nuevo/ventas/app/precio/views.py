from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from app.precio.forms import precioForm
from app.precio.models import precio

# Create your views here.


def precio_view(request):
	
	if request.method == 'POST':
		form = precioForm(request.POST)
	
		if form.is_valid():
			form.save()
		return redirect('precio:precio_listar')
	
	else:
		form = precioForm()
	
		return render(request,'precio/precio_form.html',{'form':form})


def precio_list(request):

	pr=precio.objects.all()
	contexto = {'precio':pr}
	return render(request,'precio/precio_list.html',contexto)


def precio_edit(request,id_precio):

	pr = precio.objects.get(id=id_precio)

	if request.method == 'GET':
		form = precioForm(instance=pr)

	else:
		form = precioForm (instante=pr)
		if form.is_valid():
			form.save()
		return redirect('precio:precio_listar')
	
	return render(request,'precio/precio_form.html',{'form':form})


def precio_delete(request,id_precio):

	pr=precio.objects.get(id=id_precio)
	if request.method == 'POST':
		pr.delete()
		return redirect('precio:precio_listar')
	return render(request,'precio/precio_delete.html',{'precio':pr})
