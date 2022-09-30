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
    













    #PRIMERA ENTREGA
    #INICIO
    path("perros/", perros, name="perros"),
    path("gatos/", gatos, name="gatos"),
    path("usuarios/", adoptantes, name="usuarios"),
    #FORMULARIOS
    path("perrosformulario/", perrosformulario, name="perrosformulario"),
    path("gatosformulario/", gatosformulario, name="gatosformulario"),
    path("usuariosformulario/", usuariosformulario, name="usuariosformulario"),
    #BUSQUEDA
    path("perrosbuscar/", perrosbuscar, name="perrosbuscar"),
    path("gatosbuscar/", gatosbuscar, name="gatosbuscar"),
    path("usuariosbuscar/", usuariosbuscar, name="usuariosbuscar"),
    #RESULTADOS
    path("pbuscar/", pbuscar, name="pbuscar"),
    path("gbuscar/", gbuscar, name="gbuscar"),
    path("ubuscar/", ubuscar, name="ubuscar"),
]