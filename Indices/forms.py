# indices/forms.py
from django import forms
from .models import Indice, LugarRecomendado, ComentarioLugar

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


class ComentarioLugarForm(forms.ModelForm):
    class Meta:
        model = ComentarioLugar
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Escribe tu comentario...', 
                'rows': 2,
                'cols': 40
            }),
        }
