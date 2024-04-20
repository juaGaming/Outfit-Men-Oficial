from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


#Registrar Usuarios
def RegistrarUsuarios(request):
    if request.method == 'GET':
        return render(request, 'Registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                #login(request, user)
                return redirect('Iniciar_Sesion')
            except IntegrityError:
                return render(request, 'Registro.html', {"form": UserCreationForm, "error": "ya existe un usuario con este nombre."})

        return render(request, 'Registro.html', {"form": UserCreationForm, "error": "las contraseñas no coinciden."})
    

#Iniciar Sesion
def Iniciar_Sesion(request):
    if request.method == 'GET':
        return render(request, 'Login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('InventarioAdmin')

#cerrar sesion
@login_required
def Cerrar_Sesion(request):
    logout(request)
    return redirect('Page_Inicio')