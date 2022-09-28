from django.urls import path
from blog.views import *

urlpatterns = [
    
    #INICIO
    path("", iniciosinlogin, name="iniciosinlogin"),
    path("", inicio, name="inicio"),
    path("perros/", perros, name="perros"),
    path("gatos/", gatos, name="gatos"),
    path("usuarios/", adoptantes, name="usuarios"),
    path("sobrenosotros/", sobrenosotros, name="sobrenosotros"),
   
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