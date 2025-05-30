from django import forms
from .models import Turn

class TurnForm(forms.ModelForm):
    class Meta:
        model = Turn
        fields = ['client', 'barber', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
        }