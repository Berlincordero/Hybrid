from django import forms
from .models import Planta, Vivero, Monitoreo, Mapa, Bodega, Empleado, Gasto

class ViveroForm(forms.ModelForm):
    class Meta:
        model = Vivero
        fields = ['nombre', 'espacio_total']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [
            'nombre', 
            'descripcion', 
            'fecha_adquisicion',  
            'tipo',
            'variedad', 
            'sistema_cultivo', 
            'calidad_suelo', 
            'sistema_riego',
            'tipo_poda', 
            'exposicion',
            'area_sembrar',
            'imagen'
        ]
        labels = {
            'fecha_adquisicion': 'Fecha de siembra',
            'exposicion': 'Exposición solar',
            'area_sembrar': 'Área de siembra por metro cuadrado',
            'dias_cosecha': 'Días estimados para cosecha',
        }
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'area_sembrar': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'dias_cosecha': forms.NumberInput(attrs={'class': 'form-input', 'step': '1'}),
        }

class MonitoreoForm(forms.ModelForm):
    class Meta:
        model = Monitoreo
        fields = ['observacion']
        labels = {
            'observacion': 'Observaciones Semanales',
        }
        widgets = {
            'observacion': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Escribe tu observación para esta semana...',
                'rows': 3
            }),
        }

class PlantaImagenForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['imagen']

class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nombre', 'descripcion', 'tamano_terreno', 'cantidad_sectores', 'topografia', 'imagen']
        labels = {
            'nombre': 'Nombre de sembradio',
            'descripcion': 'Descripción',
            'tamano_terreno': 'Tamaño del terreno para cultivo (m²)',
            'cantidad_sectores': 'Cantidad de sectores o sembradios',
            'topografia': 'Topografía del terreno',
            'imagen': 'Imagen o foto',
        }

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['tipo', 'descripcion', 'tamano', 'imagen']
        labels = {
            'tipo': 'Tipo de Bodega',
            'descripcion': 'Descripción',
            'tamano': 'Tamaño de la Bodega metros cuadrados',
            'imagen': 'Imagen',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Descripción de la bodega...', 'rows': 3}),
            'tamano': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre_completo',
            'tareas',
            'horario',
            'direccion',
            'telefono',
            'correo',
            'whatsapp',
            'salario',
            'profesion',
            'servicios_requeridos',
            'imagen'
        ]
        labels = {
            'nombre_completo': 'Nombre Completo del Empleado',
            'tareas': 'Tareas asignadas',
            'horario': 'Horario',
            'direccion': 'Dirección',
            'telefono': 'Teléfono de contacto',
            'correo': 'Correo de contacto',
            'whatsapp': 'Whatsapp',
            'salario': 'Salario',
            'profesion': 'Profesión o estudios',
            'servicios_requeridos': 'Servicios requeridos',
            'imagen': 'Imagen o foto',
        }
        
class GastoForm(forms.ModelForm):
      class Meta:
        model = Gasto
        fields = ['fecha', 'nombre', 'descripcion', 'lista_productos', 'total_gasto', 'tipo_transaccion', 'factura']
        labels = {
            'fecha': 'Fecha',
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'lista_productos': 'Lista de Productos',
            'total_gasto': 'Gastos en Total',
            'tipo_transaccion': 'Tipo de Transacción',
            'factura': 'Imagen de la Factura',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'lista_productos': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'total_gasto': forms.TextInput(attrs={'class': 'form-input'}),
            'tipo_transaccion': forms.Select(attrs={'class': 'form-input'}),
        }