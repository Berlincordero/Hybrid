from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'imagen', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Descripción detallada...'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Precio'
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Categoría (ej: Frutas, Hortalizas, Granos)'
            }),
            # El campo imagen usará el widget por defecto (archivo) y se estilizará con CSS si es necesario.
        }
