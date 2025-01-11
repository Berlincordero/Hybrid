# Perfiles/models.py
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ACTIVIDAD_COMERCIAL_CHOICES = [
        ('agropecuaria', 'Agropecuaria'),
        ('ganaderia', 'Ganadería'),
        ('venta_insumos', 'Venta de Insumos'),
        ('otros', 'Otros'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="Biografía")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ubicación")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    actividad_comercial = models.CharField(
        max_length=50,
        choices=ACTIVIDAD_COMERCIAL_CHOICES,
        default='otros',
        verbose_name="Actividad Comercial"
    )
    foto_perfil = models.ImageField(
        upload_to='perfiles_fotos/',
        blank=True,
        null=True,
        verbose_name="Foto de Perfil"
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"
