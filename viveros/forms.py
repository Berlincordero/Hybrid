from django import forms
from .models import Planta

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'descripcion', 'fecha_adquisicion', 'tipo', 'imagen']
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
        }
