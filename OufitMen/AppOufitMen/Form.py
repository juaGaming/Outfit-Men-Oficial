from .models import *
from django.contrib.auth.forms import *
from .models import Usuario
from django import forms



#LoginUsuarios

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('Usu_Documento', 'Usu_Nombre', 'Usu_Apellido', 'Usu_Correo')
        


class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(widget=forms.PasswordInput)