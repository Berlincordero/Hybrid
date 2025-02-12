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
    
      # Nuevo campo para los servicios que brinda la finca
    servicios = models.TextField(
        blank=True,
        null=True,
        help_text="Lista de servicios que brinda la finca"
    )
    
    # Nuevo campo para el tipo de actividad
    TIPO_ACTIVIDAD_CHOICES = [
        ('comercial', 'Comercial'),
        ('turistica', 'Turística'),
        ('recreacional', 'Recreacional (sin fines de lucro)'),
    ]
    tipo_actividad = models.CharField(
        max_length=20,
        choices=TIPO_ACTIVIDAD_CHOICES,
        blank=True,
        null=True,
        help_text="Selecciona el tipo de actividad"
    )


    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"
