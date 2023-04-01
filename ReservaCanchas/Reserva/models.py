from django.db import models

# Create your models here.
class Persona (models.Model):
    nombre   = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula   = models.CharField(max_length=10)
    correo   = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)

class Cancha(models.Model):
    nombre          = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    esta_disponible = models.BooleanField(default=True)