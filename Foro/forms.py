from django import forms
from .models import Foro, Comentario

class ForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['titulo', 'contenido_texto', 'imagen', 'video', 'post_type']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-900 text-white border border-green-500 rounded-lg placeholder-gray-500',
                'placeholder': 'Título o Contenido del foro...'
            }),
            'contenido_texto': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-900 text-white border border-green-500 rounded-lg placeholder-gray-500',
                'placeholder': 'Contenido...',
                'rows': 4
            }),
            'post_type': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-900 text-white border border-green-500 rounded-lg'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'w-full',
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'w-full',
            }),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-900 text-white border border-green-500 rounded-lg placeholder-gray-500',
                'placeholder': 'Escribe tu comentario...',
                'rows': 2
            })
        }
