from django.urls import path
from .views import lista_empleados, registrar_empleados

urlpatterns = [
    path('', lista_empleados, name='lista_empleados'),
    path('registrar/', registrar_empleados, name='registrar_empleados'),
]