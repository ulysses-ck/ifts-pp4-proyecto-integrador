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
    def validate_unique(self):
        # Sobrescribe la validación de unicidad para ignorarla
        pass
    def clean_email(self):
        """
        Permite que el email ya exista si solo se está reutilizando, sin levantar error.
        """
        email = self.cleaned_data['email']
        # No hacer validación de unicidad en el formulario, se maneja en la vista
        return email