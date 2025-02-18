from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import Producto 
from .forms import ProductoForm 


def lista_productos(request): 
    productos = Producto.objects.all() 
    return render(request, 'lista_productos.html', {'productos': productos}) 

def registrar_producto(request): 
    if request.method == 'POST': 
        form = ProductoForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_productos') 
    else: 
        form = ProductoForm() 
    return render(request, 'registrar_producto.html', {'form': form}) 

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request, exception):
    return render(request, '500.html', status=500)

