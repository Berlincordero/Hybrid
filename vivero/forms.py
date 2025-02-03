# forms.py
from django import forms
from .models import Planta, Vivero

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
            'fecha_adquisicion',  # Este campo mostrará "Fecha de siembra"
            'tipo',
            'variedad', 
            'sistema_cultivo', 
            'calidad_suelo', 
            'sistema_riego',
            'tipo_poda', 
            'exposicion',         # Este campo mostrará "Exposición solar"
            'area_sembrar',       # Este campo mostrará "Área de siembra por metro cuadrado"
            'espacio_requerido',  # Este campo mostrará "Espacio requerido metro cuadrado"
            'consumo_agua',       # Este campo mostrará "Consumo de agua por litro por día"
            'consumo_fertilizante',  # Este campo mostrará "Consumo de fertilizante por gramos"
            'imagen'
        ]
        labels = {
            'fecha_adquisicion': 'Fecha de siembra',
            'exposicion': 'Exposición solar',
            'area_sembrar': 'Área de siembra por metro cuadrado',
            'espacio_requerido': 'Espacio requerido metro cuadrado',
            'consumo_agua': 'Consumo de agua por litro por día Calculado',
            'consumo_fertilizante': 'Consumo de fertilizante por gramos',
        }
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'area_sembrar': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'espacio_requerido': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'consumo_agua': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
            'consumo_fertilizante': forms.NumberInput(attrs={'class': 'form-input', 'step': 'any'}),
        }
