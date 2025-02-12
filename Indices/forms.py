# indices/forms.py
from django import forms
from .models import Indice

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
