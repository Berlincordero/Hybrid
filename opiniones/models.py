from django.db import models
from django.contrib.auth.models import User

class Opinion(models.Model):
    autor = models.ForeignKey(
        User,
        related_name='opiniones',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200, blank=True)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Las más recientes primero

    def __str__(self):
        return self.titulo if self.titulo else f"Opinión de {self.autor.username} a las {self.created_at:%d/%m/%Y %H:%M}"
