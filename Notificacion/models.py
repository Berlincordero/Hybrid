from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Notificacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField()
    enlace = models.URLField(blank=True, null=True)  # Enlace opcional relacionado con la notificación
    leido = models.BooleanField(default=False)  # Estado de lectura
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return f"Notificación para {self.user.username}: {self.titulo}"
