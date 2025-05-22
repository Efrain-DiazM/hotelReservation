from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email_contacto = models.EmailField()
    categoria_estrellas = models.PositiveSmallIntegerField()
    descripcion_general = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre