from django import forms
from .models import Turn

class TurnForm(forms.ModelForm):
    class Meta:
        model = Turn
        fields = ['client', 'barber', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
