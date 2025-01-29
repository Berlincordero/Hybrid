# marketplace/forms.py

from django import forms
from .models import (
    FrutasVerduras,
    Animales,
    Ganado,
    Propiedades,
    Vehiculos,
    Insumos,
)

class FrutasVerdurasForm(forms.ModelForm):
    class Meta:
        model = FrutasVerduras
        fields = [
            'categoria',
            'titulo',
            'descripcion',
            'precio',
            'moneda',
            'ubicacion',
            'telefono',
            'whatsapp',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }

class AnimalesForm(forms.ModelForm):
    class Meta:
        model = Animales
        fields = [
            'categoria',
            'titulo',     # Tipo de Animal
            'descripcion',
            'edad',       # Cantidad
            'raza',
            'moneda',
            'precio',
            'ubicacion',
            'telefono',
            'whatsapp',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }

class GanadoForm(forms.ModelForm):
    class Meta:
        model = Ganado
        fields = [
            'categoria',
            'tipo',
            'descripcion',
            'cantidad',
            'edad',
            'enfermedades',
            'raza',
            'genetica',
            'pureza',
            'raza_padres',
            'numero_areteo',
            'peso',
            'moneda',
            'precio',
            'ubicacion',
            'telefono',
            'whatsapp',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }

class PropiedadesForm(forms.ModelForm):
    class Meta:
        model = Propiedades
        fields = [
            'categoria',
            'titulo',
            'descripcion',
            'tipo_propiedad',
            'moneda',
            'precio_por_metro_cuadrado',
            'precio',
            'ubicacion',
            'telefono',
            'whatsapp',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }

class VehiculosForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = [
            'categoria',
            'titulo',
            'descripcion',
            'tipo_vehiculo',
            'tipo_transmision',
            'kilometraje',
            'titulo_de_propiedad',
            'modelo',
            'ubicacion',
            'precio',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = [
            'categoria',
            'titulo',
            'descripcion',
            'precio',
            'moneda',
            'ubicacion',
            'telefono',
            'whatsapp',
            'actas_venta_nacimiento',
            'video',
        ]
        widgets = {
            'categoria': forms.HiddenInput(),
        }
