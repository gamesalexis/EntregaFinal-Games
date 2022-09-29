from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse
from blog.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# INICIO

def iniciologin(request):
    return render (request, "blog/iniciologin.html")

@login_required
def inicio(request):
    return render (request, "blog/inicio.html" ,{"avatar":obteneravatar(request)})

def perros(request):
    return render (request, "blog/perros.html")
def gatos(request):
    return render (request, "blog/gatos.html")
def adoptantes(request):
    return render (request, "blog/usuarios.html")


# SECCION SOBRE NOSOTROS

def sobrenosotros(request):
    return render (request, "blog/sobrenosotros.html")

# SECCION LOGIN

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'blog/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "blog/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "blog/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "blog/login.html", {"formulario":form})


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "blog/login.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "blog/register.html", {"formulario":form, "mensaje":"Formulario Invalido"})
    else:
        form=UserRegisterForm()
        return render(request, "blog/register.html", {"formulario":form})

@login_required
def perfil(request):    
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "blog/inicio.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "blog/perfil.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "blog/perfil.html", {"formulario":form, "usuario":usuario, "avatar":obteneravatar(request)})


@login_required
def agregaravatar(request):
    if request.method=='POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'blog/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "avatar": avatar.imagen.url})
        else:
            return render(request, 'blog/agregaravatar.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO'})
        
    else:
        formulario=AvatarForm()
        return render(request, "blog/agregaravatar.html", {"formulario":formulario, "usuario":request.user, "avatar": obteneravatar(request)})

def obteneravatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.jpg"
    return imagen





# SECCION FORMULARIOS

def perrosformulario(request):

    if request.method=="POST":
        form= PerrosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Raza= info["Raza"]
            Tamano= info["Tamano"]
            Edad= info["Edad"]
            Perro= Perros(Nombre=Nombre, Raza=Raza, Tamano=Tamano, Edad=Edad)
            Perro.save()
            return render (request, "blog/perros.html", {"mensaje":"Perro Cargado exitosamente!"})
    else:
        form= PerrosFormulario()
        return render(request, "blog/perrosformulario.html", {"formulario":form})


def gatosformulario(request):

    if request.method=="POST":
        form= GatosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Raza= info["Raza"]
            Tamano= info["Tamano"]
            Edad= info["Edad"]
            Gato= Gatos(Nombre=Nombre, Raza=Raza, Tamano=Tamano, Edad=Edad)
            Gato.save()
            return render (request, "blog/gatos.html", {"mensaje":"Gato Cargado exitosamente!"}) 
    else:
        form= GatosFormulario()
        return render(request, "blog/gatosformulario.html", {"formulario":form})


def usuariosformulario(request):

    if request.method=="POST":
        form= UsuariosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Nombre= info["Nombre"]
            Apellido= info["Apellido"]
            Sueldo= info["Sueldo"]
            Edad= info["Edad"]
            Direccion= info["Direccion"]
            Email= info["Email"]
            Usuario= Usuarios(Nombre=Nombre, Apellido=Apellido, Sueldo=Sueldo, Edad=Edad, Direccion=Direccion, Email=Email)
            Usuario.save()
            return render (request, "blog/usuarios.html", {"mensaje":"Usuario Cargado exitosamente!"})
    else:
        form= UsuariosFormulario()
        return render(request, "blog/usuariosformulario.html", {"formulario":form})


#SECCION BUSQUEDA


def perrosbuscar(request):
    return render(request, "blog/perrosbuscar.html")

def pbuscar(request):

    if request.GET["raza"]:
        Raza=request.GET["raza"]
        Perro=Perros.objects.filter(Raza=Raza)
        return render(request, "blog/perrosresultados.html", {"Perro":Perro})
    else:
        return render(request, "blog/perrosbuscar.html", {"mensaje":"No se encuentra Perro"})

def gatosbuscar(request):
    return render(request, "blog/gatosbuscar.html")

def gbuscar(request):

    if request.GET["edad"]:
        Edad=request.GET["edad"]
        Gato=Gatos.objects.filter(Edad=Edad)
        return render(request, "blog/gatosresultados.html", {"Gato":Gato})
    else:
        return render(request, "blog/gatosbuscar.html", {"mensaje":"No se encuentra Gato"})


def usuariosbuscar(request):
    return render(request, "blog/usuariosbuscar.html")

def ubuscar(request):

    if request.GET["nombre"]:
        Nombre=request.GET["nombre"]
        Usuario=Usuarios.objects.filter(Nombre=Nombre)
        return render(request, "blog/usuariosresultados.html", {"Usuario":Usuario})
    else:
        return render(request, "blog/usuariosbuscar.html", {"mensaje":"No se encuentra Usuario"})