from django.db import models
from django.contrib.auth.models import User

# Opciones para campo categoría y tipo de ganado
CATEGORIAS = (
    ('frutas_verduras', 'Frutas y Verduras'),
    ('ganado', 'Ganado'),
    ('propiedades', 'Propiedades'),
    ('vehiculos', 'Vehículos'),
    ('insumos', 'Insumos'),
    ('servicios', 'Servicios Profesionales'),
)

TIPO_GANADO = (
    ('engorde', 'Engorde'),
    ('cria', 'Cría'),
    ('lechera', 'Lechera'),
    ('semental', 'Semental'),
    ('reproductivo', 'Reproductivo'),
    ('trabajo', 'Trabajo'),
)

class Producto(models.Model):
    vendedor = models.ForeignKey(User, related_name='productos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    modelo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.TextField()
    precio_por_metro_cuadrado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(
        max_length=10,
        choices=(
            ('colones', 'Colones'),
            ('pesos', 'Pesos'),
            ('euros', 'Euros'),
            ('dolares', 'Dólares'),
        ),
        default='dolares'
    )
    tipo_propiedad = models.CharField(
        max_length=20,
        choices=(
            ('finca', 'Finca'),
            ('quinta', 'Quinta'),
            ('lote', 'Lote'),
            ('Casa', 'Casa'),
        ),
        default='finca'
    )
    tipo_vehiculo = models.CharField(
        max_length=20,
        choices=(
            ('sedan', 'Sedan'),
            ('pickub', 'Pickup'),
            ('camion', 'Camión'),
            ('trabajo', 'Trabajo'),
        ),
        default='sedan'
    )
    tipo_transmision = models.CharField(
        max_length=20,
        choices=(
            ('manual', 'Manual'),
            ('automatica', 'Automática'),
        ),
        default='manual'
    )
    kilometraje = models.IntegerField(blank=True, null=True)
    titulo_de_propiedad = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    whatsapp = models.CharField(max_length=30, blank=True, null=True)
    tipo_ganado = models.CharField(max_length=20, choices=TIPO_GANADO, blank=True, null=True)
    enfermedades = models.TextField(blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    genetica = models.CharField(max_length=200, blank=True, null=True)
    pureza = models.CharField(max_length=100, blank=True, null=True)
    razas_padres = models.CharField(max_length=200, blank=True, null=True)
    numero_areteo = models.CharField(max_length=100, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='productos/actas/', blank=True, null=True)
    marca_propiedad = models.ImageField(upload_to='productos/marca_propiedad/', blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/imagenes/')

    def __str__(self):
        return f"Imagen de {self.producto.titulo}"

class VideoProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='productos/videos/')

    def __str__(self):
        return f"Video de {self.producto.titulo}"
