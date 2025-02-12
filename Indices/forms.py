# indices/forms.py
from django import forms
from .models import Indice
from .models import LugarRecomendado

class IndiceForm(forms.ModelForm):
    class Meta:
        model = Indice
        fields = [
            'main_categoria',
            'sub_categoria',
            'fecha',
            'porcentaje',
            'antes',
            'sube',
            'total',
            'precio_actual',
            'inflacion',
            'image'
        ]


class LugarRecomendadoForm(forms.ModelForm):
    class Meta:
        model = LugarRecomendado
        fields = ['nombre', 'direccion', 'descripcion', 'precio', 'imagen', 'url']