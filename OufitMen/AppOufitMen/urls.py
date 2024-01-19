from django.urls import path   ## busca en el sistema corre los elementos
from . views import* ##llama los metodos
from django.conf.urls.static import *## configuracion de los archivos estaticos
from .import views

urlpatterns = [
    # Otras URL de tu aplicación
    path('InventarioAdmin',views.InventarioAdmin,name="VistaInventarioAdmin"),
    path('InsertarPrendas/',InsertarProducto.as_view(),name='InsertarPrendas'),
]
