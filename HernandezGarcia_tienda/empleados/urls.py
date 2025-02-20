from django.urls import path
from .views import lista_empleados, registrar_empleados, prueba_error, exception_form, error_handler

urlpatterns = [
    path('', lista_empleados, name='lista_empleados'),
    path('registrar/', registrar_empleados, name='registrar_empleados'),
    path("error/", prueba_error, name="error"),
    path("formulario-excepciones/", exception_form, name="exception_form"),
    path("error/<str:error_code>/<str:error_message>/", error_handler, name="error_handler"),

]