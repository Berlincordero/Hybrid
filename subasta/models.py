# subasta/models.py

from django.db import models
from django.contrib.auth.models import User

class Subasta(models.Model):
    TIPO_CHOICES = [
        ('ganado', 'Ganado'),
        ('caballo', 'Caballo'),
        ('chancho', 'Chancho'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    precio_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    precio_reserva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='subastas/', blank=True, null=True)

    video = models.FileField(upload_to='subastas/videos/', blank=True, null=True)
    document = models.FileField(upload_to='subastas/docs/', blank=True, null=True)

    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"


class SubastaImagen(models.Model):
    subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='subastas/images/')

    def __str__(self):
        return f"Imagen de {self.subasta.titulo}"


class Oferta(models.Model):
    subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE, related_name='ofertas')
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Oferta de {self.comprador.username} por {self.monto}"
