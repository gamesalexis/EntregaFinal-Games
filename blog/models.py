from django.db import models

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
