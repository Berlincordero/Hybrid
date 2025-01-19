from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    vendedor = models.ForeignKey(
        User,
        related_name='productos',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo
