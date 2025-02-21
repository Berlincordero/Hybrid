from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, localdate

class Vivero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vivero')
    nombre = models.CharField(max_length=255, default="Mi Vivero")
    espacio_total = models.FloatField(help_text="Espacio total del vivero en m²")

    def espacio_disponible(self):
        espacio_ocupado = sum(planta.area_sembrar for planta in self.plantas.all() if planta.area_sembrar)
        return self.espacio_total - espacio_ocupado

    def __str__(self):
        return f"Vivero de {self.usuario.username}"

class Planta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantas')
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name='plantas', null=True, blank=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_adquisicion = models.DateField(default=now)  # Fecha de siembra
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

    # Campos de cultivo
    variedad = models.CharField(
        max_length=50,
        choices=[
            ('tomate', 'Tomate'),
            ('lechuga', 'Lechuga'),
            ('zanahoria', 'Zanahoria'),
            ('vainica', 'Vainica'),
            ('calabaza', 'Calabaza'),
        ],
        null=True,
        blank=True,
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
    )
    area_sembrar = models.FloatField(
        help_text="Área destinada para este cultivo en m² (dentro del total del vivero)",
        null=True,
        blank=True
    )
    dias_cosecha = models.IntegerField(
        default=120,
        help_text="Días estimados para que la planta esté lista"
    )
    block_num = models.PositiveIntegerField(
        default=1,
        help_text="Número de bloque o sembradio donde se siembra esta planta"
    )

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"

    def dias_transcurridos(self):
        return (localdate() - self.fecha_adquisicion).days

    def dias_restantes(self):
        restantes = self.dias_cosecha - self.dias_transcurridos()
        return 0 if restantes < 0 else restantes

    @property
    def necesita_actualizacion_foto(self):
        dias = self.dias_transcurridos()
        return dias >= 7 and dias % 7 == 0

class Monitoreo(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='monitoreos')
    fecha = models.DateField(auto_now_add=True)
    observacion = models.TextField(help_text="Observaciones semanales")

    def __str__(self):
        return f"Monitoreo {self.id} - {self.planta.nombre} ({self.fecha})"

class Mapa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mapas')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    tamano_terreno = models.FloatField(help_text="Tamaño del terreno para cultivo en m²")
    cantidad_sectores = models.PositiveIntegerField(help_text="Cantidad de sectores o sembradios")
    TOPOGRAFIA_CHOICES = [
        ('plano', 'Plano'),
        ('semiplano', 'Semiplano'),
        ('quebrado', 'Quebrado'),
        ('pendiente', 'Pendiente'),
        ('inclinado', 'Inclinado'),
    ]
    topografia = models.CharField(max_length=50, choices=TOPOGRAFIA_CHOICES)
    imagen = models.ImageField(upload_to='mapas/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Bodega(models.Model):
    TIPO_CHOICES = [
        ('insumos', 'Insumos'),
        ('almacenamiento', 'Almacenamiento'),
        ('herramientas', 'Herramientas'),
        ('varios', 'Varios'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bodegas')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    tamano = models.FloatField(help_text="Tamaño de la bodega (en m²)")
    imagen = models.ImageField(upload_to='bodegas/', blank=True, null=True)

    def __str__(self):
        return f"Bodega ({self.get_tipo_display()}) - {self.usuario.username}"
    
    
class Empleado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='empleados')
    nombre_completo = models.CharField(max_length=255)
    tareas = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    salario = models.CharField(max_length=50, blank=True, null=True)  # Tipo cadena para poder poner "120000 colones"
    profesion = models.CharField(max_length=255, blank=True, null=True)
    servicios_requeridos = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='empleados/', blank=True, null=True)

    def __str__(self):
        return self.nombre_completo
    
class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos')
    fecha = models.DateField(default=now)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    lista_productos = models.TextField(blank=True, null=True)
    total_gasto = models.CharField(max_length=50, blank=True, null=True)  # Ahora es string
    TIPO_TRANSACCION_CHOICES = [
        ('gasto', 'Gasto'),
        ('venta', 'Venta'),
        ('mantenimiento', 'Mantenimiento'),
        ('equipo', 'Equipo'),
        ('inversion', 'Inversión'),
        ('planilla', 'Planilla'),
        ('servicios', 'Servicios'),
        ('insumos', 'Insumos'),
    ]
    tipo_transaccion = models.CharField(max_length=50, choices=TIPO_TRANSACCION_CHOICES)
    factura = models.ImageField(upload_to='gastos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_transaccion_display()}) - {self.usuario.username}"
