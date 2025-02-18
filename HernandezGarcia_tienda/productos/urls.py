from django.urls import path
from .views import lista_productos, registrar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('registrar/', registrar_producto, name='registrar_producto'),
]