from django.db import models
from hoteles.models import Hotel
from habitaciones.models import Habitacion

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion_servicio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_servicio

class HotelServicio(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hotel', 'servicio')

class RoomServicio(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('habitacion', 'servicio')