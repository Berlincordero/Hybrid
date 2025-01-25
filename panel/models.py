from django.db import models
from django.contrib.auth.models import User

class Configuracion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='configuracion')
    tema = models.CharField(
        max_length=50,
        choices=[
            ('oscuro', 'Modo Oscuro'),
            ('claro', 'Modo Claro'),
        ],
        default='oscuro'
    )
    idioma = models.CharField(
        max_length=50,
        choices=[
            ('es', 'Español'),
            ('en', 'Inglés'),
            ('fr', 'Francés'),
        ],
        default='es'
    )
    notificaciones = models.BooleanField(default=True)
    actualizaciones_automaticas = models.BooleanField(default=False)

    def __str__(self):
        return f"Configuración de {self.usuario.username}"
