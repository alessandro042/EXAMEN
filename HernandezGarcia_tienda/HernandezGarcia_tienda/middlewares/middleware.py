import logging
from django.http import JsonResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except ValueError as e:  # Excepción específica
            logger.error(f"Error de Valor: {str(e)}")
            return JsonResponse({"error": "Dato inválido"}, status=400)
        except Exception as e:  # Cualquier otro error
            logger.error(f"Error Interno: {str(e)}", exc_info=True)
            
            # Si es una API, devolver JSON
            if request.headers.get("Content-Type") == "application/json":
                return JsonResponse({"error": "Error interno del servidor"}, status=500)

            # Si es una página web, redirigir a un HTML personalizado
            return render(request, "500.html", status=500)
