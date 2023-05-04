from django.db import models
from django.utils import timezone

# Create your models here.

class Concierto(models.Model):
    nombre = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    fecha = models.DateTimeField(default=timezone.now)

class Localidad(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    concierto = models.ForeignKey(Concierto, on_delete=models.PROTECT)
    capacidad = models.IntegerField(default=5)
    cantidad_disponible = models.IntegerField(default=capacidad)

class Ticket(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    concierto = models.ForeignKey(Concierto, on_delete=models.PROTECT)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    fecha_compra = models.DateTimeField(auto_now_add=True)

