from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Planta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantas')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateField(default=now)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('ornamental', 'Ornamental'),
            ('frutal', 'Frutal'),
            ('aromaticas', 'Aromáticas'),
            ('hortalizas', 'Hortalizas'),
        ]
    )
    imagen = models.ImageField(upload_to='viveros/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"
