from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Nombre completo',
            'email': 'Correo electrónico',
            'phone': 'Teléfono',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ingresa tu nombre completo',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'tu.email@ejemplo.com',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Ej: +54 9 11 1234-5678',
                'class': 'form-control'
            }),
        }