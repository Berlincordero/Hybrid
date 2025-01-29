# marketplace/models.py

from django.db import models
from django.contrib.auth.models import User

# Definición de opciones
MONEDA_CHOICES = [
    ('colones', 'Colones'),
    ('pesos', 'Pesos'),
    ('euros', 'Euros'),
    ('dolares', 'Dólares'),
]

TIPO_PROPIEDAD_CHOICES = [
    ('finca', 'Finca'),
    ('quinta', 'Quinta'),
    ('lote', 'Lote'),
    ('casa', 'Casa'),
]

TIPO_VEHICULO_CHOICES = [
    ('sedan', 'Sedan'),
    ('pickup', 'Pickup'),
    ('camion', 'Camión'),
    ('trabajo', 'Agrícola/Trabajo/Herramienta'),
]

TRANSMISION_CHOICES = [
    ('manual', 'Manual'),
    ('automatico', 'Automático'),
]

class FrutasVerduras(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='frutas_verduras')
    categoria = models.CharField(max_length=50, default="frutas_verduras")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA_CHOICES, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.titulo}"


class Animales(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animales')
    categoria = models.CharField(max_length=50, default="animales")
    titulo = models.CharField(max_length=200, blank=True, null=True)  # Tipo de Animal
    descripcion = models.TextField(blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)  # Cantidad
    raza = models.CharField(max_length=200, blank=True, null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA_CHOICES, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.titulo}"


class Ganado(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ganado')
    categoria = models.CharField(max_length=50, default="ganado")
    tipo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    edad = models.CharField(max_length=100, blank=True, null=True)  # Ejemplo: "2 años"
    enfermedades = models.CharField(max_length=200, blank=True, null=True)
    raza = models.CharField(max_length=200, blank=True, null=True)
    genetica = models.CharField(max_length=200, blank=True, null=True)
    pureza = models.CharField(max_length=200, blank=True, null=True)
    raza_padres = models.CharField(max_length=200, blank=True, null=True)
    numero_areteo = models.CharField(max_length=200, blank=True, null=True)
    peso = models.CharField(max_length=100, blank=True, null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA_CHOICES, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.tipo}"


class Propiedades(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='propiedades')
    categoria = models.CharField(max_length=50, default="propiedades")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_propiedad = models.CharField(max_length=50, choices=TIPO_PROPIEDAD_CHOICES, blank=True, null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA_CHOICES, blank=True, null=True)
    precio_por_metro_cuadrado = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.titulo}"


class Vehiculos(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehiculos')
    categoria = models.CharField(max_length=50, default="vehiculos")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_vehiculo = models.CharField(max_length=50, choices=TIPO_VEHICULO_CHOICES, blank=True, null=True)
    tipo_transmision = models.CharField(max_length=50, choices=TRANSMISION_CHOICES, blank=True, null=True)
    kilometraje = models.CharField(max_length=100, blank=True, null=True)
    titulo_de_propiedad = models.CharField(max_length=200, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.titulo}"


class Insumos(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insumos')
    categoria = models.CharField(max_length=50, default="insumos")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=20, choices=MONEDA_CHOICES, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    actas_venta_nacimiento = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.titulo}"
