from django.db import models
from django.contrib.auth.models import AbstractUser

class Empleado(models.Model):  
    nombre_completo = models.CharField(max_length=100) 
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.CharField(max_length=100)


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Gerente'),
        ('employee', 'Empleado'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.username