from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'attachment']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-800 text-white rounded-md',
                'placeholder': 'Escribe tu mensaje...'
            })
        }
