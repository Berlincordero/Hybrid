# indices/forms.py
from django import forms
from .models import Indice, LugarRecomendado

class IndiceForm(forms.ModelForm):
    class Meta:
        model = Indice
        fields = [
            'main_categoria',
            'sub_categoria',
            'nombre',          # <-- Campo agregado
            'antes',
            'sube',           # <-- Este ahora es un select con "sube" o "baja"
            'total',
            'precio_actual',
            'fuente',
            'inflacion',
            'image'
        ]

class LugarRecomendadoForm(forms.ModelForm):
    class Meta:
        model = LugarRecomendado
        fields = ['nombre', 'direccion', 'descripcion', 'precio', 'imagen', 'url']
