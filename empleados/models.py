from django.db import models
from hoteles.models import Hotel

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)
    descripcion_rol = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_rol

class Empleado(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"