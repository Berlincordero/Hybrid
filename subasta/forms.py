from django import forms
from .models import Subasta, Oferta

class SubastaForm(forms.ModelForm):
    class Meta:
        model = Subasta
        fields = ['titulo', 'descripcion', 'tipo', 'precio_inicial', 'imagen', 'fecha_inicio', 'fecha_fin']

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['monto']
