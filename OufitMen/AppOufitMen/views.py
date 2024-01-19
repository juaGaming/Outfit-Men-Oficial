# views.py

import json
from typing import Any
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Producto
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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

def InventarioAdmin(request): 
    return render (request, "InventarioAdmin.html")
    