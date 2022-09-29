from django.db import models
from django.contrib.auth.models import User

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

#ENTREGA FINAL 

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')
