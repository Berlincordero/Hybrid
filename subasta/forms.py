# subasta/forms.py

from django import forms
from django.utils import timezone
from .models import Subasta, Oferta, SubastaImagen
from .widgets import ClearableMultipleFileInput

class SubastaForm(forms.ModelForm):
    """
    Formulario para crear/editar Subasta.
    Incluye un campo 'imagenes' especial para subir múltiples imágenes.
    """
    imagenes = forms.FileField(
        widget=ClearableMultipleFileInput(attrs={'multiple': True}),
        required=False,
        label="Imagen(es)"
    )

    class Meta:
        model = Subasta
        fields = [
            'titulo',
            'descripcion',
            'tipo',
            'precio_inicial',
            'precio_reserva',
            'video',
            'document',
            'fecha_inicio',
            'fecha_fin',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Título de la subasta'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Descripción (opcional)',
                'rows': 4
            }),
            'tipo': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500'
            }),
            'precio_inicial': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Precio inicial'
            }),
            'precio_reserva': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Precio de reserva (base)'
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500'
            }),
            'document': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500'
            }),
            'fecha_inicio': forms.DateTimeInput(attrs={
                'class': 'w-full p-2 border border-gray-700 rounded focus:ring-2 focus:ring-blue-500',
                'type': 'datetime-local'
            }),
            'fecha_fin': forms.DateTimeInput(attrs={
                'class': 'w-full p-2 border border-gray-700 rounded focus:ring-2 focus:ring-blue-500',
                'type': 'datetime-local'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        # Validación simple: que fecha_fin sea posterior a fecha_inicio
        if fecha_inicio and fecha_fin and fecha_fin <= fecha_inicio:
            self.add_error('fecha_fin', 'La fecha de fin debe ser posterior a la fecha de inicio.')

        return cleaned_data


class OfertaForm(forms.ModelForm):
    """
    Formulario para realizar ofertas en una subasta.
    """
    class Meta:
        model = Oferta
        fields = ['monto']
        widgets = {
            'monto': forms.NumberInput(attrs={
                # Estilos en modo oscuro
                'class': 'w-full p-2 border border-gray-700 bg-gray-800 text-white rounded focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Monto de la oferta'
            }),
        }
