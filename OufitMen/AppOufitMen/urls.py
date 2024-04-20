from django.urls import path   ## busca en el sistema corre los elementos
from . views import* ##llama los metodos **
from .viewsLogin import*
from .import viewsLogin
from django.conf.urls.static import *## configuracion de los archivos estaticos
from .import views
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView



#para llamar los metodos = [ logica ] 
#debemos verificar en las Views que exista y asi generar un url por cada uno

urlpatterns = [
    #Vistas Administrador
    path('InventarioAdmin',views.InventarioAdmin,name="InventarioAdmin"),
    path('InsertarPrendas/',InsertarProducto.as_view(),name='InsertarPrendas'),
    path('listarPrendas',ListarPrendas.as_view(), name='listarPrendas'),
    path('ActualizarProducto/<int:pk>',ActualizarProducto.as_view(), name='ActualizarProducto'),
    path('BuscarProducto/<int:pk>/', views.BuscarProducto.as_view(), name='BuscarProducto'),
    path('EliminarPrendas/<int:pk>',EliminarPrendas.as_view(),name='eliminar'),
    
    #Vistas Libres
    path('',views.Inicio, name="Page_Inicio"),
    path('Casual/',views.Casual, name="RegistroUsuario"),
    path('Urban/',views.Urban, name="RegistroUsuario"),
    path('Formal/',views.Formal, name="RegistroUsuario"),

    #Autenticacion
    path('Iniciar_Sesion/',viewsLogin.Iniciar_Sesion, name="Iniciar_Sesion"),
    path('RegistroUsuario/',viewsLogin.RegistrarUsuarios, name="RegistroUsuario"),
    path('Cerrar_Sesion/',viewsLogin.Cerrar_Sesion, name="RegistroUsuario"),

    
]
