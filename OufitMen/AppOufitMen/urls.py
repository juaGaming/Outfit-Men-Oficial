from django.urls import path   ## busca en el sistema corre los elementos
from . views import* ##llama los metodos **
from . viewsUsuario import*
from django.conf.urls.static import *## configuracion de los archivos estaticos
from .import views
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView



#para llamar los metodos = [ logica ] 
#debemos verificar en las Views que exista y asi generar un url por cada uno

urlpatterns = [
    # Otras URL de tu aplicación
    path('Inicio',views.Inicio, name="Page_Inicio"),
    path('RegistroUsuario/',views.registro, name="Registro"),
    path('iniciarSesion/',IniciarSesionView.as_view(),name="iniciar_sesion"),
    path('InventarioAdmin',views.InventarioAdmin,name="InventarioAdmin"),
    path('InsertarPrendas/',InsertarProducto.as_view(),name='InsertarPrendas'),
    path('listarPrendas',ListarPrendas.as_view(), name='listarPrendas'),
    path('ActualizarProducto/<int:pk>',ActualizarProducto .as_view(), name='ActualizarProducto'),
    path('BuscarProducto/<int:pk>/', views.BuscarProducto.as_view(), name='BuscarProducto'),
    path('EliminarPrendas/<int:pk>',EliminarPrendas.as_view(),name='eliminar'),
    
    #Llamamos el metodo para cargar el menu inicio
    path('',views.Inicio,name="VistaInicio"),
    
    #inicio
    path('Registro',views.Registro, name="Registro_Usuario"),


    
]
