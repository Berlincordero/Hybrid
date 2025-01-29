# marketplace/admin.py

from django.contrib import admin
from .models import (
    FrutasVerduras,
    Animales,
    Ganado,
    Propiedades,
    Vehiculos,
    Insumos,
)

@admin.register(FrutasVerduras)
class FrutasVerdurasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('titulo', 'descripcion')

@admin.register(Animales)
class AnimalesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('titulo', 'descripcion')

@admin.register(Ganado)
class GanadoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('tipo', 'descripcion')

@admin.register(Propiedades)
class PropiedadesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('titulo', 'descripcion')

@admin.register(Vehiculos)
class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('titulo', 'descripcion')

@admin.register(Insumos)
class InsumosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'vendedor', 'precio', 'vendido', 'created_at')
    search_fields = ('titulo', 'descripcion')
