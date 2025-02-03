# models.py
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
    espacio_requerido = models.FloatField(help_text="Espacio requerido por la planta (por unidad) en m²")
    consumo_agua = models.FloatField(help_text="Consumo de agua semanal en litros")
    consumo_fertilizante = models.FloatField(help_text="Consumo de fertilizante mensual en gramos")

    # Nuevos campos para el cultivo virtual
    variedad = models.CharField(
        max_length=50,
        choices=[
            ('tomate', 'Tomate'),
            ('lechuga', 'Lechuga'),
            ('zanahoria', 'Zanahoria'),
            ('ejote', 'Ejote'),
            ('calabaza', 'Calabaza'),
            # Agrega más variedades según necesites
        ],
        null=True,
        blank=True,
        help_text="Seleccione la variedad o especie (por ejemplo, tomate)"
    )
    sistema_cultivo = models.CharField(
        max_length=50,
        choices=[
            ('hileras', 'Hileras'),
            ('surcos', 'Surcos'),
            ('tutorados', 'Tutorados'),
            ('mixto', 'Mixto')
        ],
        null=True,
        blank=True,
        help_text="Seleccione el sistema de cultivo a utilizar"
    )
    calidad_suelo = models.CharField(
        max_length=50,
        choices=[
            ('alta', 'Alta'),
            ('media', 'Media'),
            ('baja', 'Baja')
        ],
        null=True,
        blank=True,
        help_text="Calidad del suelo para el cultivo"
    )
    sistema_riego = models.CharField(
        max_length=50,
        choices=[
            ('goteo', 'Goteo'),
            ('aspersión', 'Aspersión'),
            ('manual', 'Manual')
        ],
        null=True,
        blank=True,
        help_text="Método de riego que se aplicará"
    )
    tipo_poda = models.CharField(
        max_length=50,
        choices=[
            ('regular', 'Regular'),
            ('intensiva', 'Intensiva'),
            ('ninguna', 'Ninguna')
        ],
        null=True,
        blank=True,
        help_text="Tipo de poda que se aplicará al cultivo"
    )
    exposicion = models.CharField(
        max_length=50,
        choices=[
            ('alta', 'Alta'),
            ('media', 'Media'),
            ('baja', 'Baja')
        ],
        null=True,
        blank=True,
        help_text="Nivel de exposición solar en el área de siembra"
    )
    area_sembrar = models.FloatField(
        help_text="Área destinada para este cultivo en m² (dentro del total del vivero)",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"

