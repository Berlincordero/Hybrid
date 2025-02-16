# Indices/models.py
from django.db import models

# Indices/models.py
from django.db import models

class Indice(models.Model):
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

    # Opciones para el campo "sube" (select con sube o baja)
    SUBE_BAJA_CHOICES = (
        ('sube', 'Sube'),
        ('baja', 'Baja'),
    )

    pais = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="País al que corresponde el índice"
    )
    main_categoria = models.CharField(
        max_length=20,
        choices=MAIN_CATEGORIES,
        help_text="Seleccione la categoría principal."
    )
    sub_categoria = models.CharField(
        max_length=20,
        choices=SUBCATEGORIAS_PRODUCTOS,
        blank=True, 
        null=True,
        help_text="Solo para Productos: seleccione una subcategoría."
    )
    fecha = models.DateField(help_text="Fecha del índice")

    # Nuevo campo "nombre"
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre o descripción breve del índice"
    )

    # Se reemplaza el integer sube por un campo con choices
    sube = models.CharField(
        max_length=4,
        choices=SUBE_BAJA_CHOICES,
        default='sube',
        help_text="Indica si el índice sube o baja"
    )

    antes = models.IntegerField(help_text="Valor 'Antes' (por ejemplo, 56)")
    total = models.IntegerField(help_text="Valor 'Total' (por ejemplo, 80)")
    precio_actual = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio actual (por ejemplo, 100.00)"
    )
    
    # Nuevo campo "fuente"
    fuente = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Fuente de la información (opcional)"
    )

    # Se elimina porcentaje y se usa solo inflacion como porcentaje principal
    inflacion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Porcentaje de Inflación (por ejemplo, 33.00)"
    )

    image = models.ImageField(
        upload_to='indices/',
        blank=True,
        null=True,
        help_text="Imagen representativa (opcional)"
    )

    def __str__(self):
        # Muestra la categoría y fecha; también podrías incluir nombre si gustas
        return f"{self.nombre} - {self.get_main_categoria_display()} ({self.fecha})"

class LugarRecomendado(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio promedio")
    imagen = models.ImageField(upload_to='lugares/', blank=True, null=True)
    url = models.URLField(blank=True, null=True, help_text="Sitio web del lugar (opcional)")

    def __str__(self):
        return self.nombre


    

   