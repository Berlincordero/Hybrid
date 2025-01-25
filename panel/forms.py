from django import forms
from .models import Configuracion

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['tema', 'idioma', 'notificaciones', 'actualizaciones_automaticas']
