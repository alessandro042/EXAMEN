from django.db import models

class Empleado(models.Model):  
    nombre_completo = models.CharField(max_length=100) 
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.CharField(max_length=100)