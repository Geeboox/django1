from django.shortcuts import render,redirect
from django.http import HttpResponse




from app.precio.models import precio
from app.precio.forms import precioForm




# Create your views here.




def index_precio(request):         
	return render(request,'precio/index.html')





def precio_view(request):

	if request.method == 'POST':
		form = precioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('precio:precio_lista')
	else:
		form = precioForm()
	return render(request,'precio/precio_form.html',{'form':form})




def precio_list(request):

	precio=precio.objects.all()

	contexto = {'precio':precio}
	return render(request,'precio/precio_list.html',contexto)




def precio_edit(request,id_precio):

	precio = precio.objects.get(id=id_precio)
	
	if request.method == 'GET':
		form = precioForm(instance=precio)
	else:
		form = precioForm (instante=precio)
		if form.is_valid():
			 form.save()
		return redirect('precio:precio_listar')
	return render(request,'precio/precio_form.html',{'form':form})



def precio_delete(request,id_precio):
	
	precio=precio.objects.get(id=id_precio)
	if request.method == 'POST':
		precio.delete()
		return redirect('precio:precio_listar')
	return render(request,'precio/precio_delete.html',{'precio':precio})





