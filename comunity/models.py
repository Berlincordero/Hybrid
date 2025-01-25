from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    administrador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grupos_administrados')
    miembros = models.ManyToManyField(User, related_name='grupos', blank=True)
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='publicaciones')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"
