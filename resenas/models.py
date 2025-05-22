from django.db import models
from reservas.models import Reserva

class Resena(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    puntuacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha_resena = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"Reseña {self.id} - {self.puntuacion}"