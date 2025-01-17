from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Título (opcional)'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Comparte tu opinión acerca de cómo mejorar la plataforma...'
            }),
        }
