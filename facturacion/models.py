from django.db import models
from reservas.models import Reserva
from empleados.models import Empleado

class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    empleado_emisor = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    iva_decimal = models.DecimalField(max_digits=4, decimal_places=2)
    estado_pago = models.CharField(max_length=20, default='Pendiente')

class ItemFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    referencia_pago = models.CharField(max_length=100, blank=True, null=True)