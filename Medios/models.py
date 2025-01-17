from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    autor = models.ForeignKey(
        User,
        related_name='videos',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo
