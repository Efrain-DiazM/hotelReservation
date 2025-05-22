from django.db import models
from hoteles.models import Hotel

class TipoHabitacion(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    capacidad_max = models.PositiveIntegerField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_tipo

class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero_habitacion = models.CharField(max_length=10)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)

    class Meta:
        unique_together = ('hotel', 'numero_habitacion')

    def __str__(self):
        return f"{self.hotel.nombre} - {self.numero_habitacion}"