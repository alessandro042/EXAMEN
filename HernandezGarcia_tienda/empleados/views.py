from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import Empleado 
from .forms import EmpleadoForm 
from django.http import JsonResponse
import math
from django.conf import settings


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

    from django.http import JsonResponse

def prueba_error(request):
    raise ValueError("Este es un error de prueba")

def exception_form(request):
    if request.method == "POST":
        try:
            num1 = request.POST.get("num1")
            num2 = request.POST.get("num2")
            operation = request.POST.get("operation", "dividir")
            
            num1 = float(num1) if num1 else None
            num2 = float(num2) if num2 else None
            
            if num1 is None or (num2 is None and operation != "raiz"):
                raise ValueError("Uno o más valores están vacíos.")

            result = num1 + num2  # Aquí generará TypeError si los valores son incorrectos

            if operation not in ["dividir", "multiplicar", "sumar", "restar", "raiz"]:
                raise NotImplementedError(f"La operación '{operation}' no está soportada.")
            
            if operation == "dividir":
                result = num1 / num2  # Puede generar ZeroDivisionError
            elif operation == "multiplicar":
                result = num1 * num2
            elif operation == "sumar":
                result = num1 + num2
            elif operation == "restar":
                result = num1 - num2
            elif operation == "raiz":
                result = math.sqrt(num1)  # Puede generar ValueError si num1 < 0
            else:
                raise NotImplementedError("Operación no soportada.")
            
            return render(request, "exception_form.html", {"result": result})
        except ZeroDivisionError as e:
            return redirect("error_handler", error_code="ZeroDivisionError", error_message=str(e))
        except ValueError as e:
            return redirect("error_handler", error_code="ValueError", error_message=str(e))
        except TypeError as e:
            return redirect("error_handler", error_code="TypeError", error_message=str(e))
        except NotImplementedError as e:
            return redirect("error_handler", error_code="NotImplementedError", error_message=str(e))
        except Exception as e:
            return redirect("error_handler", error_code="Exception", error_message=str(e))
    
    return render(request, "exception_form.html")

def error_handler(request, error_code, error_message):
    error_messages = {
        "ZeroDivisionError": ("División entre cero", "Intentaste dividir un número entre 0, lo cual no está permitido en matemáticas."),
        "ValueError": ("Valor no válido", "Ingresaste un valor incorrecto o dejaste un campo vacío."),
        "TypeError": ("Error de tipo", "Parece que intentaste operar con datos incompatibles, como texto en lugar de números."),
        "NotImplementedError": ("Operación no soportada", "Elegiste una operación que aún no ha sido implementada."),
        "Exception": ("Error desconocido", "Ocurrió un error inesperado. Puede ser un problema en el código.")
    }
    
    error_title, error_description = error_messages.get(error_code, ("Error desconocido", "Ocurrió un problema inesperado."))
    context = {"error_title": error_title, "error_description": error_description, "error_code": error_code, "error_message": error_message}
    return render(request, "error_page.html", context)
    error_messages = {
        "ZeroDivisionError": ("División entre cero", "Intentaste dividir un número entre 0, lo cual no está permitido en matemáticas."),
        "ValueError": ("Valor no válido", "Ingresaste un valor incorrecto o dejaste un campo vacío."),
        "TypeError": ("Error de tipo", "Parece que intentaste operar con datos incompatibles, como texto en lugar de números."),
        "NotImplementedError": ("Operación no soportada", "Elegiste una operación que aún no ha sido implementada."),
        "Exception": ("Error desconocido", "Ocurrió un error inesperado. Puede ser un problema en el código.")
    }
    
    error_title, error_description = error_messages.get(error_code, ("Error desconocido", "Ocurrió un problema inesperado."))
    context = {"error_title": error_title, "error_description": error_description}
    return render(request, "error_page.html", context)
    context = {"error_message": error_message}
    return render(request, "error_page.html", context)
    context = {"error": None, "result": None}
    
    if request.method == "POST":
        try:
            num1 = request.POST.get("num1")
            num2 = request.POST.get("num2")
            operation = request.POST.get("operation", "dividir")
            
            # Intentamos convertir los valores a float, lo que podría generar ValueError
            num1 = float(num1) if num1 else None
            num2 = float(num2) if num2 else None
            
            if num1 is None or (num2 is None and operation != "raiz"):
                raise ValueError("Uno o más valores están vacíos.")
            
            if operation == "dividir":
                result = num1 / num2  # Puede generar ZeroDivisionError
            elif operation == "multiplicar":
                result = num1 * num2
            elif operation == "sumar":
                result = num1 + num2
            elif operation == "restar":
                result = num1 - num2
            elif operation == "raiz":
                result = math.sqrt(num1)  # Puede generar ValueError si num1 < 0
            else:
                raise NotImplementedError("Operación no soportada.")
            
            context["result"] = result
        except ZeroDivisionError:
            context["error"] = "Error: No se puede dividir entre 0."
        except ValueError as ve:
            context["error"] = f"Error de valor: {ve}"
        except TypeError:
            context["error"] = "Error: Se ingresaron valores no numéricos."
        except NotImplementedError as nie:
            context["error"] = f"Error: {nie}"
        except Exception as e:
            context["error"] = f"Error inesperado: {str(e)}"
    
    return render(request, "exception_form.html", context)
    context = {"error": None, "result": None}
    
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1", 0))
            num2 = float(request.POST.get("num2", 1))
            operation = request.POST.get("operation", "dividir")
            
            if operation == "dividir":
                result = num1 / num2  # Puede generar división por cero
            elif operation == "multiplicar":
                result = num1 * num2
            elif operation == "sumar":
                result = num1 + num2
            elif operation == "restar":
                result = num1 - num2
            elif operation == "raiz":
                if num1 < 0:
                    raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
                result = num1 ** 0.5
            else:
                raise NotImplementedError("Operación no soportada.")
            
            context["result"] = result
        except ZeroDivisionError:
            context["error"] = "No se puede dividir entre 0. Verifica los valores ingresados."
        except ValueError as ve:
            context["error"] = f"Entrada inválida: {ve}"
        except NotImplementedError as nie:
            context["error"] = f"Error: {nie}"
        except Exception as e:
            context["error"] = f"Ocurrió un error inesperado: {str(e)}"
    
    return render(request, "exception_form.html", context)

def perfil_actual(request):
    perfil = {
        'perfil': settings.ENVIRONMENT,  # Obtén el entorno actual
        'debug': settings.DEBUG,         # Obtén el valor de DEBUG
        'nivel_log': settings.LOG_LEVEL  # Obtén el nivel de log
    }
    return render(request, 'perfil.html', {'perfil': perfil})
