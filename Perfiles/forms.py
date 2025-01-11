# Perfiles/forms.py
from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'location', 'birth_date', 'actividad_comercial', 'foto_perfil']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400',
                'placeholder': 'Escribe algo sobre ti...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400',
                'placeholder': 'Tu ubicación'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-indigo-500 text-gray-300'
            }),
            'actividad_comercial': forms.Select(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-indigo-500 text-gray-300'
            }),
            'foto_perfil': forms.ClearableFileInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-gray-300'
            }),
        }
