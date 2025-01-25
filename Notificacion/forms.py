from django import forms
from .models import Notificacion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['user', 'titulo', 'mensaje', 'enlace', 'leido']
