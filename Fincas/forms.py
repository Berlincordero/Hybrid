from django import forms
from .models import Finca

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre', 'ubicacion', 'descripcion', 'tamaño', 'imagen', 'servicios', 'tipo_actividad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'servicios': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ej: Venta de productos orgánicos, tours guiados, etc.'}),
            'tipo_actividad': forms.Select(),
        }
