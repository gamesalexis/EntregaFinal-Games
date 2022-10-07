
from tkinter import Widget
from turtle import textinput
from django import forms 
from django.contrib.auth.forms import  *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .models import *


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
        fields = [ 'first_name', 'last_name','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


#AVATAR

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")


#PUBLICACIONES 

class PublicacionesFormulario(forms.ModelForm):
    

    imagen= forms.ImageField(label="Imagen")
    class Meta:
        model = Publicaciones
        fields = ['nombre', 'edad','especie','raza', 'descripcion']



