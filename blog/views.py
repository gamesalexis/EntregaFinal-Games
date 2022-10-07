from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# INICIO

def iniciologin(request):
    mascotas=Publicaciones.objects.all()
    print(list(mascotas))
    return render(request, "blog/iniciologin.html", {'mascotas':mascotas, "imagen":obtenerimagen(request)})

@login_required
def inicio(request):
    mascotas=Publicaciones.objects.all()
    print(list(mascotas))
    return render(request, "blog/inicio.html", {'mascotas':mascotas, "avatar":obteneravatar(request)})

# OTROS

def sobrenosotros(request):
    return render (request, "blog/sobrenosotros.html")

# LOGIN-LOGOUT

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            mascotas=Publicaciones.objects.all()
            if usuario is not None:
                login(request, usuario)
                return render(request, 'blog/inicio.html', {"mascotas":mascotas,'mensaje':f"Bienvenido {usuario}","avatar":obteneravatar(request),})
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
            return render(request, "blog/login.html", {"formulario":AuthenticationForm,"mensaje":f"Usuario {username} creado correctamente",})
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
            mascotas=Publicaciones.objects.all()
            return render(request, "blog/inicio.html", {"mascotas":mascotas,"mensaje":"Perfil editado correctamente","avatar":obteneravatar(request)})
        else:
            return render(request, "blog/perfil.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "blog/perfil.html", {"formulario":form, "usuario":usuario, "avatar":obteneravatar(request)})

#Avatar

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
            mascotas=Publicaciones.objects.all()
            return render(request, 'blog/inicio.html', {'mascotas':mascotas,'usuario':request.user, 'mensaje':'avatar cambiado', "avatar": avatar.imagen.url})
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


# PUBLICACIONES

@login_required
def publicar(request):
    if request.method=="POST":
        form= PublicacionesFormulario(request.POST, request.FILES)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            edad= info["edad"]
            descripcion= info["descripcion"]
            especie= info["especie"]
            raza= info["raza"]
            mascota= Publicaciones(user=request.user, imagen=form.cleaned_data['imagen'], nombre=nombre,edad=edad, descripcion=descripcion, especie=especie, raza=raza)
            mascota.save()
            mascotas=Publicaciones.objects.filter(user=request.user)
            return render(request, "blog/publicaciones.html", {'usuario':request.user, "mensaje":'Publicacion Realizada con Exito', "mascotas":mascotas})
        else:
            return render(request, 'blog/publicar.html', {'formulario':form,'mensaje':'Formulario Invalido', "avatar":obteneravatar(request)})
    else:
        form= PublicacionesFormulario()
        return render(request, "blog/publicar.html", {'formulario':form, "avatar":obteneravatar(request)})


@login_required
def mostrarpublicacion(request, id):
    mascota=Publicaciones.objects.get(id=id)
    print(mascota)
    return render(request, "blog/mostrarpublicacion.html", {'mascota':mascota, "imagen":obtenerimagen(request),"avatar":obteneravatar(request)})

@login_required
def publicaciones(request):
    mascotas=Publicaciones.objects.filter(user=request.user)
    print(list(mascotas))
    return render(request, "blog/publicaciones.html", {'mascotas':mascotas,"avatar":obteneravatar(request)})

@login_required
def obtenerimagen(request):
    lista=Publicaciones.objects.filter(user=request.user)
    if lista != 0:
        for img in range(len(lista)):
            print(img)
            imagen=lista[img].imagen.url
    return imagen

@login_required
def eliminarpublicacion(request, id):
    mascota=Publicaciones.objects.get(id=id)
    mascota.delete()
    mascotas=Publicaciones.objects.filter(user=request.user)
    return render(request, "blog/publicaciones.html", {"mascotas":mascotas, "avatar":obteneravatar(request)})



@login_required
def editarpublicacion(request, id):
    mascota=Publicaciones.objects.get(id=id)
    if request.method=="POST":
        form= PublicacionesFormulario(request.POST, request.FILES)
        if form.is_valid():
            info= form.cleaned_data
            mascota.nombre= info["nombre"]
            mascota.edad= info["edad"]
            mascota.descripcion= info["descripcion"]
            mascota.imagen=info["imagen"]
            mascota.especie= info["especie"]
            mascota.raza= info["raza"]
            mascota.save()
            mascotas=Publicaciones.objects.filter(user=request.user)
            return render(request, "blog/publicaciones.html", {'usuario':request.user, "mensaje":'Edicion Realizada con Exito', "mascotas":mascotas})
    else:
        form= PublicacionesFormulario(initial={"nombre":mascota.nombre, "edad":mascota.edad, "especie":mascota.especie, "raza":mascota.raza, "descripcion":mascota.descripcion,}) #"imagen":mascota.imagen,})
        return render(request, 'blog/editarpublicacion.html', {'formulario':form,'mascota':mascota, "avatar":obteneravatar(request)})

# SECCION BUSQUEDA

@login_required
def buscar(request):
    
    return render(request, "blog/buscar.html",{ "avatar":obteneravatar(request)})
@login_required
def pbuscar(request):
    form= PublicacionesFormulario(request.GET)
    if form.is_valid():
        info= form.cleaned_data
        especie= info["especie"]
        mascotas=Publicaciones.objects.filter(especie=especie)
        return render(request, "blog/inicio.html", {"mascotas":mascotas, "avatar":obteneravatar(request)})
    else:
        mascotas=Publicaciones.objects.all()
        return render(request, "blog/inicio.html", {"mensaje":"No se encuentra Perro"})
