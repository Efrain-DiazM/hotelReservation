from django.db import models
from clientes.models import Cliente
from habitaciones.models import Habitacion
from empleados.models import Empleado

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    empleado_checkin = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='checkin_reservas')
    empleado_checkout = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='checkout_reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_checkin = models.DateField()
    fecha_checkout = models.DateField()
    numero_adultos = models.PositiveIntegerField()
    numero_ninos = models.PositiveIntegerField(default=0)
    estado_reserva = models.CharField(max_length=20, default='Pendiente')
    costo_total_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"