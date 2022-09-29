from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class PerrosFormulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Raza= forms.CharField(max_length=50)
    Tamano=forms.CharField(max_length=50)
    Edad= forms.IntegerField()
        
class GatosFormulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Raza= forms.CharField(max_length=50)
    Tamano=forms.CharField(max_length=50)
    Edad= forms.IntegerField()

class UsuariosFormulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Apellido= forms.CharField(max_length=50)
    Sueldo=forms.CharField(max_length=50)
    Edad= forms.IntegerField()
    Direccion= forms.CharField(max_length=50)
    Email= forms.EmailField()

#ULTIMA ENTREGA

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}