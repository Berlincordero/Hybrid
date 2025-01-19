from django import forms
from .models import Foro, Comentario

class ForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['titulo', 'contenido_texto', 'imagen', 'video', 'post_type']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título del foro'
            }),
            'contenido_texto': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Contenido...'
            }),
            'post_type': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded'
            }),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
           'contenido': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Escribe tu comentario...',
                'rows': 2  # Ajusta el número de filas para hacerlo más pequeño
            })
        }
