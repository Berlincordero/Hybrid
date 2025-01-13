from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
     # Nuevos campos
    nombre_empresa = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nombre de la Empresa o Pymes"
    )
    anio_fundacion = models.DateField(
        blank=True,
        null=True,
        verbose_name="Año de Fundación"
    )
    actividad_economica = models.CharField(max_length=255, blank=True, null=True)
    preferencias_agropecuarias = models.CharField(max_length=255, blank=True, null=True)
    preferencias_comerciales = models.CharField(max_length=255, blank=True, null=True)
    youtube_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Enlace de YouTube"
    )
      # NUEVO CAMPO PARA INSTAGRAM
    instagram_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Enlace de Instagram"
    )
    whatsapp_link = models.URLField(
        max_length=500, 
        blank=True,
        null=True,
        verbose_name="Enlace de WhatsApp"
        )

    def __str__(self):
        return f"Perfil de {self.user.username}"

