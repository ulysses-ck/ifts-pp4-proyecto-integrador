from django import forms
from apps.Usuarios.models import User

class RegisterForm(forms.ModelForm):
    role = forms.ChoiceField(choices=User.ROLES, widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'role') 

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Aseguramos que se encripte la contraseña
        if commit:
            user.save()
        return user    
 

# Formulario de login
class LoginForm(forms.Form):
        username = forms.CharField(max_length=150, label="Nombre de usuario")
        password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")