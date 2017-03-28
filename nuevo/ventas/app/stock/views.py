from django.shortcuts import render,redirect
from app.stock.forms import stockForm
from app.stock.models import stock



# Create your views here.

def stock_view(request):

	if request.method == 'POST':
		form = stockForm(request.POST)
		if form.is_valid():
			 form.save()
		return redirect('stock:stock_listar')
	
	else:
		form = stockForm()
		return render(request,'stock/stock_form.html',{'form':form})



def stock_list(request):

	pr=stock.objects.all()
	contexto = {'stock':pr}

	return render(request,'stock/stock_list.html',contexto)



def stock_edit(request,id_stock):

	pr = stock.objects.get(id=id_stock)
	
	if request.method == 'GET':
		form = stockForm(instance=pr)
	
	else:
		form = stockForm (instante=pr)
		if form.is_valid():
			form.save()
		return redirect('stock:stock_listar')
	
	return render(request,'stock/stock_form.html',{'form':form})


def stock_delete(request,id_stock):

	pr=stock.objects.get(id=id_stock)
	if request.method == 'POST':
		pr.delete()
		return redirect('stock:stock_listar')
	return render(request,'stock/stock_delete.html',{'stock':pr})




