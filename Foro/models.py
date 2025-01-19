from django.db import models
from django.contrib.auth.models import User

POST_TYPE_CHOICES = (
    ('text', 'Texto'),
    ('image', 'Imagen'),
    ('video', 'Video'),
)

class Foro(models.Model):
    autor = models.ForeignKey(
        User,
        related_name="foros",
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    # Se guarda el contenido textual; se usará si es post de tipo "text"
    contenido_texto = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="foro/images/", blank=True, null=True)
    video = models.FileField(upload_to="foro/videos/", blank=True, null=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default="text")
    # La relación ManyToMany permite que varios usuarios marquen la publicación con estrella
    estrellas = models.ManyToManyField(User, related_name="foros_estrellados", blank=True)
    reposted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_estrellas(self):
        return self.estrellas.count()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    foro = models.ForeignKey(Foro, related_name="comentarios", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, related_name="comentarios", on_delete=models.CASCADE)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.foro.titulo}"
