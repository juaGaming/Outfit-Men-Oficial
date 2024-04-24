# views.py
import json
from typing import Any
from django.http import JsonResponse
from django.views import View
from .models import Producto
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from .Form import UsuarioCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .Form import *
from .Form import LoginForm




    #metodo para insertar Prendas
class InsertarProducto(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error en el ID"})
        datos=json.loads(request.body)
       
        prod_Nombre = datos.get('prod_Nombre')
        prod_Descripcion = datos.get('prod_Descripcion')
        prod_Precio = datos.get('prod_Precio')
        prod_Talla = datos.get('prod_Talla')
        prod_Color = datos.get('prod_Color')
        prod_Imagen=datos.get('prod_Imagen')
        print("datos",request.POST)
        Producto.objects.create(prod_Nombre=prod_Nombre,prod_Descripcion=prod_Descripcion,prod_Precio=prod_Precio,prod_Talla=prod_Talla,prod_Color=prod_Color,prod_Imagen=prod_Imagen)
        return JsonResponse({"mensaje":"Datos Guardados"})

def Casual(request):
    return render (request, "Casual.html")

def Formal(request):
    return render (request, "Formal.html")

def Urban(request):
    return render (request, "Urban.html")
@login_required
def InventarioAdmin(request): 
    context = {'username': request.user.username}
    return render (request, "InventarioAdmin.html",context)

def Inicio(request): 
    return render (request, "inicio.html")    
    
    
def Registro(request):
    return render (request, "Registro.html")




#metodo para listar Prendas
class ListarPrendas(View):
    def get(self, request):
        datos = Producto.objects.all()
        Datos_Producto = []
        for i in datos:
            Datos_Producto.append({
                'prod_Id': i.prod_Id,
                'prod_Nombre': i.prod_Nombre,
                'prod_Descripcion': i.prod_Descripcion,
                'prod_Precio': i.prod_Precio,
                'prod_Talla': i.prod_Talla,
                'prod_Color': i.prod_Color,
                'prod_Imagen': i.prod_Imagen.url if i.prod_Imagen else None  # Obtener la URL de la imagen
            })
        return JsonResponse(Datos_Producto, safe=False, encoder=DjangoJSONEncoder)

#metodo para buscar prendas
class BuscarProducto(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        try:
            produc = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return JsonResponse({"Error": "El Producto no existe"})
        
        # Obtener la URL de la imagen en lugar del objeto ImageFieldFile
        prod_imagen_url = produc.prod_Imagen.url if produc.prod_Imagen else None

        datos_Producto = {
            'prod_Id': produc.prod_Id,
            'prod_Nombre': produc.prod_Nombre,
            'prod_Descripcion': produc.prod_Descripcion,
            'prod_Precio': produc.prod_Precio,
            'prod_Talla': produc.prod_Talla,
            'prod_Color': produc.prod_Color,
            'prod_Imagen': prod_imagen_url  # Usar la URL de la imagen
        }

        return JsonResponse(datos_Producto)



#metodo para actualizar prendas
class ActualizarProducto(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,pk):
            
        try:
            ActuProducto=Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return JsonResponse({"Error":"El documento no existe"})
        data=json.loads(request.body)
        ActuProducto.prod_Id=data.get('prod_Id')
        ActuProducto.prod_Nombre=data.get('prod_Nombre')
        ActuProducto.prod_Descripcion=data.get('prod_Descripcion')
        ActuProducto.prod_Precio=data.get('prod_Precio')
        ActuProducto.prod_Talla=data.get('prod_Talla')
        ActuProducto.prod_Color=data.get('prod_Color')
        ActuProducto.prod_Imagen=data.get('prod_Imagen')
        ActuProducto.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
    
    #metodo para eliminar prendas
class EliminarPrendas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            deleteProducto=Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return JsonResponse({"Error":"La prenda  no existe"})
        deleteProducto.delete()
        return JsonResponse({"Mensaje":"Prenda Eliminada"})
    

#metodo para registrar Usuario
# def registro(request):
#     if request.method == 'POST':
#         form = UsuarioCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redireccionar a una página después de un registro exitoso
#             return redirect('Page_Inicio')
#     else:
#         form = UsuarioCreationForm()
#     return render(request, 'Registro.html', {'form': form})


# from django.contrib.auth import authenticate, login

# class IniciarSesionView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'Login.html', {'form': form})

#     def post(self, request):
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             correo = form.cleaned_data.get('correo')  # Obtener el correo electrónico del formulario
#             password = form.cleaned_data.get('password')
#             print("Correo:", correo)

#             print("Correo:", correo)
#             user = authenticate(request, correo=correo, password=password)
#             print("Usuario autenticado:", user)
            
#             # Autenticar al usuario utilizando el correo electrónico y la contraseña
#             user = authenticate(request, correo=correo, password=password)
#             print("error ",user)
#             if user is not None:
#                 # Si el usuario es autenticado correctamente, iniciar sesión y redirigir
#                 login(request, user)
#                 print("Usuario autenticado:", user)
#                 return redirect('InventarioAdmin')
#             else:
#                 # Si la autenticación falla, añade un mensaje de error al formulario
#                 form.add_error(None, "Nombre de usuario o contraseña incorrectos.")

#         else:
#             # Si el formulario no es válido, imprime los errores de validación en la consola
#             print("Errores de validación:", form.errors)
#         # Si la autenticación falla, renderizar el formulario nuevamente con un mensaje de error
#         print("Autenticación fallida")
#         return render(request, 'Login.html', {'form': form})
