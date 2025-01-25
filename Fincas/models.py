from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Finca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fincas')
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=now)
    tamaño = models.FloatField(help_text="Tamaño en hectáreas")
    imagen = models.ImageField(upload_to='fincas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"
