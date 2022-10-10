from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #LOGIN OR LOGOUT
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path("perfil/", perfil, name="perfil"),
    path('agregaravatar/', agregaravatar, name='agregaravatar'),

    #OTROS
    path("sobrenosotros/", sobrenosotros, name="sobrenosotros"),
    
    #INICIO
    path("", iniciologin, name="iniciologin"),
    path("inicio", inicio, name="inicio"),
    
   #PUBLICACIONES
    path("publicaciones/", publicaciones, name="publicaciones"),
    path("publicar/", publicar, name="publicar"),
    path('eliminarpublicacion/<id>', eliminarpublicacion, name='eliminarpublicacion'),
    path('editarrpublicacion/<id>', editarpublicacion, name='editarpublicacion'),
    path('mostrarpublicacion/<id>', mostrarpublicacion, name='mostrarpublicacion'),
    path('pbuscar', pbuscar, name='pbuscar'),
    path('pbuscar2', pbuscar2, name='pbuscar2'),












]