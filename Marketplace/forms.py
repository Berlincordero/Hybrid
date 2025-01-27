from django import forms
from .models import Producto, ImagenProducto, VideoProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'titulo', 'descripcion', 'precio', 'moneda', 'categoria',
            'ubicacion', 'telefono', 'whatsapp',
            'tipo_ganado', 'enfermedades', 'raza', 'edad', 'genetica',
            'pureza', 'razas_padres', 'numero_areteo', 'actas_venta_nacimiento',
            'marca_propiedad', 'peso', 'tipo_propiedad', 'precio_por_metro_cuadrado',
            'modelo', 'tipo_vehiculo', 'titulo_de_propiedad', 'tipo_transmision',
            'kilometraje',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título del producto',
                'autofocus': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Descripción detallada...',
                'rows': 5
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Precio en moneda seleccionada'
            }),
            'moneda': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Ubicación específica'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Teléfono de contacto'
            }),
            'whatsapp': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Número de Whatsapp'
            }),
            'tipo_ganado': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'enfermedades': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Detalles sobre enfermedades (opcional)',
                'rows': 3
            }),
            'raza': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Raza del ganado'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Edad en meses o años'
            }),
            'genetica': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Información genética'
            }),
            'pureza': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Pureza del animal (opcional)'
            }),
            'razas_padres': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Razas de los padres (opcional)'
            }),
            'numero_areteo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Número de arete del ganado'
            }),
            'actas_venta_nacimiento': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'accept': 'image/*'
            }),
            'marca_propiedad': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'accept': 'image/*'
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Peso (kg)'
            }),
            'tipo_propiedad': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'precio_por_metro_cuadrado': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Precio por metro cuadrado'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Modelo / Año'
            }),
            'tipo_vehiculo': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'titulo_de_propiedad': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título de propiedad'
            }),
            'tipo_transmision': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
            }),
            'kilometraje': forms.NumberInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Kilometraje'
            }),
        }


class ImagenProductoForm(forms.ModelForm):
    class Meta:
        model = ImagenProducto
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'accept': 'image/*'
            }),
        }


class VideoProductoForm(forms.ModelForm):
    class Meta:
        model = VideoProducto
        fields = ['video']
        widgets = {
            'video': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'accept': 'video/*'
            }),
        }
