from django import forms
from .models import *
from django.contrib.auth.forms import *
from django import forms
from .models import Producto

#Formulario para insertar producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['prod_Nombre', 'prod_Descripcion', 'prod_Precio', 'prod_Talla', 'prod_Color','prod_Imagen']
