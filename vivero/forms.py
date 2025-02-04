# forms.py
from django import forms
from .models import Planta, Vivero, Monitoreo

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
            'espacio_requerido', 
            'consumo_agua', 
            'consumo_fertilizante',  
            'imagen'
        ]
        labels = {
            'fecha_adquisicion': 'Fecha de siembra',
            'exposicion': 'Exposición solar',
            'area_sembrar': 'Área de siembra por metro cuadrado',
            'espacio_requerido': 'Espacio requerido metro cuadrado',
            'consumo_agua': 'Consumo de agua por litro por día Calculado',
            'consumo_fertilizante': 'Consumo de fertilizante por gramos',
            'dias_cosecha': 'Días estimados para cosecha',
        }
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'area_sembrar': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'espacio_requerido': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'consumo_agua': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'consumo_fertilizante': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
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