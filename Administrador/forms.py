# forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'w-full sm:w-1/2 px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Apellido',
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido',
            'class': 'w-full sm:w-1/2 px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        })
    )
    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        }),
        label='Contraseña'
    )
    birth_day = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 32)],
        label='Día de nacimiento',
        widget=forms.Select(attrs={
            'class': 'w-full sm:w-1/3 px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300'
        })
    )
    birth_month = forms.ChoiceField(
        choices=[
            (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
            (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
            (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
        ],
        label='Mes de nacimiento',
        widget=forms.Select(attrs={
            'class': 'w-full sm:w-1/3 px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300'
        })
    )
    birth_year = forms.ChoiceField(
        choices=[(y, y) for y in range(1900, 2026)],
        label='Año de nacimiento',
        widget=forms.Select(attrs={
            'class': 'w-full sm:w-1/3 px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300'
        })
    )
    gender = forms.ChoiceField(
        choices=[
            ('female', 'Mujer'),
            ('male', 'Hombre'),
            ('custom', 'Personalizado')
        ],
        widget=forms.RadioSelect(attrs={
            'class': 'form-radio text-indigo-500'
        }),
        label='Género'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo ya está registrado.")
        return email

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-300 placeholder-gray-400'
        }),
        label='Contraseña'
    )
