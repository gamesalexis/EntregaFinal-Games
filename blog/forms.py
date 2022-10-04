
from tkinter import Widget
from turtle import textinput
from django import forms 
from django.contrib.auth.forms import  *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .models import *


#ULTIMA ENTREGA
#LOGIN LOGOUT
class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1= forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','email', 'password1', 'password2',]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")


#PUBLICACIONES 

class PublicacionesFormulario(forms.ModelForm):

    class Meta:
        model = Publicaciones
        fields = ['nombre', 'edad','especie','raza', 'descripcion', 'imagen']

















#PRIMERA ENTREGA
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