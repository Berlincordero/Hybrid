from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    # --- Código original intacto ---
    autor = models.ForeignKey(
        User,
        related_name='videos',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    # --- Nuevos campos ---
    CATEGORIAS = [
        ("NOTICIAS", "Noticias"),
        ("CURSOS", "Cursos"),
        ("CONSEJOS", "Consejos"),
        ("BLOGGER", "Bloger"),
        ("PUBLICITARIO", "Publicitario"),
        ("SERVICIOS_PROFESIONALES", "Servicios Profesionales"),
        ("PERSONAL", "Personal"),
    ]
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default="PERSONAL"
    )
    vistas = models.PositiveIntegerField(default=0)
    estrellas = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo

class VideoComment(models.Model):
    """Nuevo modelo para comentarios de los videos."""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user} en {self.video}"
