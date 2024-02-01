from django.urls import path   ## busca en el sistema corre los elementos
from . views import* ##llama los metodos
from django.conf.urls.static import *## configuracion de los archivos estaticos
from .import views

#para llamar los metodos = [ logica ] 
#debemos verificar en las Views que exista y asi generar un url por cada uno

urlpatterns = [
    # Otras URL de tu aplicación
    path('InventarioAdmin',views.InventarioAdmin,name="VistaInventarioAdmin"),
    path('InsertarPrendas/',InsertarProducto.as_view(),name='InsertarPrendas'),
    path('listarPrendas',ListarPrendas.as_view(), name='listarPrendas'),
    path('ActualizarProducto/<int:pk>',ActualizarProducto .as_view(), name='ActualizarProducto'),
    path('BuscarProducto/<int:pk>/', views.BuscarProducto.as_view(), name='BuscarProducto'),
    path('EliminarPrendas/<int:pk>',EliminarPrendas.as_view(),name='eliminar'),
    
    
]
