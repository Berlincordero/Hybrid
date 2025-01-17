from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'video_file']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título del video'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Descripción (opcional)'
            }),
        }
