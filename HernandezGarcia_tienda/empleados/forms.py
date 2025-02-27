from django import forms
from .models import Empleado
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'sueldo', 'departamento']

    def clean_sueldo(self):
        sueldo = self.cleaned_data.get('sueldo')
        if sueldo <= 0.0 or sueldo > 12000.0:
            raise forms.ValidationError('El sueldo debe estar entre 0.0 y 12000.0')
        return sueldo

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label="Rol")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class": "form-control"}))