from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



#ENTREGA FINAL 
#LOGIN LOGOUT

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')

#PUBLICACIONES
opciones_especie=[(0, "Sin Definir"),(1, "Perro"),(2, "Gato"),(3, "Otro")]

class Publicaciones(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,blank=True, null=True)
    edad= models.IntegerField()
    descripcion=RichTextField()
    imagen= models.ImageField(upload_to='imagenes')
    especie=models.IntegerField(choices=opciones_especie)
    raza=models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.nombre















#PRIMERA ENTREGA
class Perros(models.Model):
    Nombre= models.CharField(max_length=50)
    Raza= models.CharField(max_length=50)
    Tamano=models.CharField(max_length=50)
    Edad= models.IntegerField()     
class Gatos(models.Model):
    Nombre= models.CharField(max_length=50)
    Raza= models.CharField(max_length=50)
    Tamano=models.CharField(max_length=50)
    Edad= models.IntegerField()
class Usuarios(models.Model):
    Nombre= models.CharField(max_length=50)
    Apellido= models.CharField(max_length=50)
    Sueldo= models.CharField(max_length=50)
    Edad= models.IntegerField()
    Direccion= models.CharField(max_length=50)
    Email= models.EmailField()