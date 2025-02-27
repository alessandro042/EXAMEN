from django.urls import path
from .views import lista_empleados, registrar_empleados, prueba_error, exception_form, error_handler, perfil_actual, registro_view, procesar_registro, login_view, logout_view

urlpatterns = [
    path('', lista_empleados, name='lista_empleados'),
    path('registrar/', registrar_empleados, name='registrar_empleados'),
    path("error/", prueba_error, name="error"),
    path("formulario-excepciones/", exception_form, name="exception_form"),
    path("error/<str:error_code>/<str:error_message>/", error_handler, name="error_handler"),
    path("perfil/", perfil_actual, name="perfil_actual"),
    path("registro/", registro_view, name="registro"),
    path("procesar_registro/", procesar_registro, name="procesar_registro"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]