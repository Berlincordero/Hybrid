from django import forms
from .models import Planta, Vivero

class ViveroForm(forms.ModelForm):
    class Meta:
        model = Vivero
        fields = ['nombre', 'espacio_total']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'descripcion', 'fecha_adquisicion', 'tipo', 'imagen', 'espacio_requerido', 'consumo_agua', 'consumo_fertilizante']
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
        }
