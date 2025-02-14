# Indices/models.py
from django.db import models

class Indice(models.Model):
    # Tus campos para Indice...
    MAIN_CATEGORIES = (
        ('productos', 'Productos'),
        ('insumos', 'Insumos'),
        ('animales', 'Animales'),
    )
    SUBCATEGORIAS_PRODUCTOS = (
        ('carnes', 'Carnes'),
        ('granos', 'Granos'),
        ('vegetales', 'Vegetales'),
        ('frutas', 'Frutas'),
        ('lacteos', 'Lácteos'),
    )
    pais = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        help_text="País al que corresponde el índice"
    )
    main_categoria = models.CharField(
        max_length=20, choices=MAIN_CATEGORIES,
        help_text="Seleccione la categoría principal."
    )
    sub_categoria = models.CharField(
        max_length=20, choices=SUBCATEGORIAS_PRODUCTOS,
        blank=True, null=True,
        help_text="Solo para Productos: seleccione una subcategoría."
    )
    fecha = models.DateField(help_text="Fecha del índice")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje (por ejemplo, 13.00)")
    antes = models.IntegerField(help_text="Valor 'Antes' (por ejemplo, 56)")
    sube = models.IntegerField(help_text="Valor 'Sube' (por ejemplo, 24)")
    total = models.IntegerField(help_text="Valor 'Total' (por ejemplo, 80)")
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio actual (por ejemplo, 100.00)")
    inflacion = models.DecimalField(max_digits=5, decimal_places=2, help_text="Inflación (por ejemplo, 33.00)")
    image = models.ImageField(upload_to='indices/', blank=True, null=True, help_text="Imagen representativa (opcional)")

    def __str__(self):
        return f"{self.get_main_categoria_display()} ({self.fecha})"

class LugarRecomendado(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio promedio")
    imagen = models.ImageField(upload_to='lugares/', blank=True, null=True)
    url = models.URLField(blank=True, null=True, help_text="Sitio web del lugar (opcional)")

    def __str__(self):
        return self.nombre
