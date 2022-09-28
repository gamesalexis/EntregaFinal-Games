from django import forms

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
