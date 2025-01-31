from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Vivero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vivero')
    nombre = models.CharField(max_length=255, default="Mi Vivero")
    espacio_total = models.FloatField(help_text="Espacio total del vivero en m²")

    def espacio_disponible(self):
        espacio_ocupado = sum(planta.espacio_requerido for planta in self.plantas.all())
        return self.espacio_total - espacio_ocupado

    def __str__(self):
        return f"Vivero de {self.usuario.username}"

class Planta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantas')
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name='plantas', null=True, blank=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateField(default=now)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('ornamental', 'Ornamental'),
            ('frutal', 'Frutal'),
            ('aromaticas', 'Aromáticas'),
            ('hortalizas', 'Hortalizas'),
        ]
    )
    imagen = models.ImageField(upload_to='viveros/', blank=True, null=True)
    espacio_requerido = models.FloatField(help_text="Espacio requerido por la planta en m²")
    consumo_agua = models.FloatField(help_text="Consumo de agua semanal en litros")
    consumo_fertilizante = models.FloatField(help_text="Consumo de fertilizante mensual en gramos")

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"
