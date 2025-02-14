# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Finca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fincas')
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=now)
    tamaño = models.FloatField(help_text="Tamaño en metros cuadrados")
    imagen = models.ImageField(upload_to='fincas/', blank=True, null=True)
    
    servicios = models.TextField(
        blank=True,
        null=True,
        help_text="Lista de servicios que brinda la finca"
    )
    
    TIPO_ACTIVIDAD_CHOICES = [
        ('comercial', 'Comercial'),
        ('turistica', 'Turística'),
        ('recreacional', 'Recreacional (sin fines de lucro)'),
    ]
    tipo_actividad = models.CharField(
        max_length=20,
        choices=TIPO_ACTIVIDAD_CHOICES,
        blank=True,
        null=True,
        help_text="Selecciona el tipo de actividad"
    )

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"


# models.py

class Division(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='divisiones')
    
    TIPO_DIVISION_CHOICES = [
        ('casa', 'Casa o estructura'),
        ('cultivo', 'Terreno de cultivo'),
        ('potrero', 'Potrero'),
        ('estanque', 'Estanque o lago'),
        ('caminos', 'Caminos'),
    ]
    tipo_division = models.CharField(max_length=50, choices=TIPO_DIVISION_CHOICES)
    
    descripcion = models.TextField(blank=True, null=True)
    
    TIPO_TERRENO_CHOICES = [
        ('plano', 'Plano'),
        ('semiplano', 'Semiplano'),
        ('irregular', 'Irregular'),
        ('empinado', 'Empinado'),
        ('terraceo', 'Terraceo'),
        ('hundido', 'Hundido'),
    ]
    tipo_terreno = models.CharField(max_length=50, choices=TIPO_TERRENO_CHOICES)
    
    tamaño = models.FloatField(help_text="Tamaño en metros cuadrados de la división")
    
    UBICACION_CHOICES = [
        ('izquierdo', 'Lado izquierdo'),
        ('derecho', 'Lado derecho'),
        ('centro', 'En el centro'),
        ('a_lo_largo', 'A lo largo'),
    ]
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES)
    
    cantidad_arboles = models.PositiveIntegerField(default=0)
    rios = models.PositiveIntegerField(default=0)
    
    # Nuevo campo para animales (ej: cantidad de vacas si es potrero)
    animales = models.PositiveIntegerField(default=0, help_text="Cantidad de animales (ej: vacas) si es un potrero")
    
    imagen = models.ImageField(upload_to='divisiones/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_tipo_division_display()} - {self.tamaño} m²"


class Galpon(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='galpones')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    tamano = models.FloatField(help_text="Tamaño global del galpón en m²")
    almacen_paja = models.CharField(
        max_length=3,
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )
    tamano_almacen_paja = models.FloatField(
        blank=True,
        null=True,
        help_text="Tamaño del almacenamiento de paja en m²"
    )
    otro_producto = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Otro tipo de producto almacenado (opcional)"
    )
    
    def __str__(self):
        return self.nombre


class GalponDivision(models.Model):
    galpon = models.ForeignKey(Galpon, on_delete=models.CASCADE, related_name='divisiones')
    animales = models.PositiveIntegerField(default=0, help_text="Cantidad de animales en la sección")
    tamano = models.FloatField(help_text="Tamaño de la división en m²")
    
    def __str__(self):
        return f"División ({self.tamano} m², {self.animales} animales)"
    
# models.py (en tu app, actualiza o agrega la siguiente clase)
class ControlAnimal(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='control_animales')
    imagen = models.ImageField(upload_to='control_animales/', blank=True, null=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del Animal")
    descripcion = models.TextField(blank=True, null=True)
    tipo_animal = models.CharField(max_length=50, help_text="Tipo de Animal")
    raza = models.CharField(max_length=100, help_text="Raza")
    peso = models.FloatField(help_text="Peso (en kg)")
    # Cambiamos de FloatField a CharField para permitir textos como "4 meses"
    edad = models.CharField(max_length=50, help_text="Edad (ej: 4 meses)")
    tipo_tratamiento = models.CharField(max_length=100, help_text="Tipo de Tratamiento")
    nombre_medicina = models.CharField(max_length=100, help_text="Nombre de la Medicina")
    # Cambiamos de FloatField a CharField para permitir textos como "1 onza" o "100 gramos"
    cantidad = models.CharField(max_length=50, help_text="Cantidad aplicada (ej: 1 onza, 100 gramos)")
    tipo_control = models.CharField(max_length=100, help_text="Tipo de Control")
    num_arete = models.CharField(max_length=50, help_text="Número de Arete o de Identificación")
    atendido_por = models.CharField(max_length=100, help_text="Nombre de quien atiende el animal")
    ubicacion = models.CharField(max_length=255, help_text="Ubicación del animal en la finca")
    fecha_control = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora del control")

    def __str__(self):
        return f"{self.nombre} ({self.tipo_animal})"