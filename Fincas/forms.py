from django import forms
from .models import Finca, Division, Galpon, GalponDivision, PersonalFinca, GastoFinca
from .models import ControlAnimal

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre', 'ubicacion', 'descripcion', 'tamaño', 'imagen', 'servicios', 'tipo_actividad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'servicios': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ej: Venta de productos orgánicos, tours guiados, etc.'}),
            'tipo_actividad': forms.Select(),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = [
            'tipo_division', 
            'descripcion', 
            'tipo_terreno', 
            'tamaño', 
            'ubicacion', 
            'cantidad_arboles', 
            'rios', 
            'animales',
            'imagen'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
        
class GalponForm(forms.ModelForm):
    class Meta:
        model = Galpon
        fields = [
            'nombre',
            'descripcion',
            'tamano',
            'almacen_paja',
            'tamano_almacen_paja',
            'otro_producto',
            'imagen',  # <-- Añadimos aquí
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class GalponDivisionForm(forms.ModelForm):
    class Meta:
        model = GalponDivision
        fields = ['animales', 'tamano']

class ControlAnimalForm(forms.ModelForm):
    class Meta:
        model = ControlAnimal
        fields = [
            'imagen', 'nombre', 'descripcion', 'tipo_animal', 'raza',
            'peso', 'edad', 'tipo_tratamiento', 'nombre_medicina', 'cantidad',
            'tipo_control', 'num_arete', 'atendido_por', 'ubicacion'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class PersonalFincaForm(forms.ModelForm):
    class Meta:
        model = PersonalFinca
        fields = [
            'nombre', 'horario', 'direccion', 'correo', 'telefono', 'whatsapp',
            'salario', 'profesion_estudios', 'servicios_requeridos', 'area_designada',
            'contrato', 'salario_por_mes', 'foto'
        ]
        widgets = {
            'servicios_requeridos': forms.Textarea(attrs={'rows': 3}),
        }
        
class GastoFincaForm(forms.ModelForm):
    class Meta:
        model = GastoFinca
        fields = [
            'descripcion',
            'lista_productos',
            'total',
            'tipo_transaccion',
            'fecha',
            'foto',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'lista_productos': forms.Textarea(attrs={'rows': 3}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }