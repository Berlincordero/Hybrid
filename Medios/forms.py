from django import forms
from .models import Video, VideoComment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'video_file', 'categoria']  # <-- se añade 'categoria'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Título del video'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Descripción (opcional)'
            }),
            # Podrías añadir un widget para 'categoria' si lo deseas:
            'categoria': forms.Select(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded'
            }),
        }

class CommentForm(forms.ModelForm):
    """Formulario para enviar comentarios a un video."""
    class Meta:
        model = VideoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white border border-gray-700 rounded',
                'placeholder': 'Escribe tu comentario...'
            }),
        }
