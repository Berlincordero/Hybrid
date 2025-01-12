from django import forms
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['fecha_nacimiento', 'biografia','nombre_empresa','anio_fundacion', 'direccion', 'actividad_economica', 'preferencias_agropecuarias', 'preferencias_comerciales']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-2 bg-gray-700 text-white rounded'
            }),
            'biografia': forms.Textarea(attrs={
                'class': '...',
                'placeholder': 'Escribe tu biografía',
            }),
             'anio_fundacion': forms.DateInput(attrs={
                'type': 'date',
                'class': '...',
                'placeholder': 'Selecciona el año',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-700 text-white rounded',
                'placeholder': 'Ciudad o dirección'
            }),
            'actividad_economica': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-700 text-white rounded',
                'placeholder': 'Actividad económica'
            }),
            'preferencias_agropecuarias': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-700 text-white rounded',
                'placeholder': 'Preferencias agropecuarias'
            }),
            'preferencias_comerciales': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-700 text-white rounded',
                'placeholder': 'Preferencias comerciales'
            }),
        }


