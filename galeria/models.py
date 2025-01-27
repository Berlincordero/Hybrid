from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Archivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archivos')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='galeria/')
    tipo = models.CharField(
        max_length=10,
        choices=[
            ('imagen', 'Imagen'),
            ('video', 'Video'),
            ('otro', 'Otro'),
        ],
        default='imagen'
    )
    fecha_subida = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.titulo} ({self.tipo}) - {self.usuario.username}"
