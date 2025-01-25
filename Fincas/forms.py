from django import forms
from .models import Finca

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre', 'ubicacion', 'descripcion', 'tamaño', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
