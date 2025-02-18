from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import Empleado 
from .forms import EmpleadoForm 


def lista_empleados(request): 
    empleados = Empleado.objects.all() 
    return render(request, 'lista_empleados.html', {'empleados': empleados}) 

def registrar_empleados(request): 
    if request.method == 'POST': 
        form = EmpleadoForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_empleados') 
    else: 
        form = EmpleadoForm() 
    return render(request, 'registrar_empleados.html', {'form': form}) 