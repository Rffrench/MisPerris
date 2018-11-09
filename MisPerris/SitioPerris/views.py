from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Usuario, Rescatado
from .forms import RegistrarUsuario, LoginLog, AgregarRescatado
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
#*********INICIAR SESIÓN CON USUARIOS CREADOS MEDIANTE COMANDO SUPERUSER*******
# Create your views here.
def index(request):
   # if request.user.is_authenticated:
   #     return redirect('inicio')
   # else:
   #     return redirect('login')
    titulo="Mis Perris | Inicio"
    return render(request,"inicio.html",{'titulo':titulo})

def salir(request):
    logout(request)
    return redirect('/')

def registroUsuarios(request):
    
    form=RegistrarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("password"))
        usuario=Usuario(user=regDB,correo=data.get("correo"),nombreCompleto=data.get("nombreCompleto"),direccionUsuario=data.get("direccionUsuario"),perfil=data.get("perfil"))
        regDB.save() 
        usuario.save()
    usuarios=Usuario.objects.all()
    form=RegistrarUsuario()
    titulo="Mis Perris | Registro Usuarios"
    return render(request,"registrousuarios.html",{'titulo':titulo,'form':form,'usuarios':usuarios})

def ingresar(request):
    titulo="Mis Perris | Login"
    form=LoginLog(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('inicio')
    return render(request,"login.html",{'form':form,'titulo':titulo})


def agregarrescatado(request):
    if request.method == 'POST':

        form=AgregarRescatado(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            rescatado=Rescatado(fotoRescatado=data.get("fotoRescatado"),nombreRescatado=data.get("nombreRescatado"),razaRescatado=data.get("razaRescatado"),descripcionRescatado=data.get("descripcionRescatado"),estadoRescatado=data.get("estadoRescatado"))
            rescatado.save()
    rescatados=Rescatado.objects.all()
    form=AgregarRescatado()
    titulo="Mis Perris | Agregar Rescatado"
    return render(request,"agregarrescatado.html",{'titulo':titulo,'form':form,'rescatados':rescatados})


#def handle_uploaded_file(f):
#    name = f.name
#
#    with open(os.path.join("static\images","{0}".format(name)),'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)

def listarrescatados(request):
    titulo="Mis Perris | Lista Rescatados"
    return render(request,"listarrescatados.html",{'titulo':titulo})


def listardisponibles(request):

    disponibles=Rescatado.object.all()
    plantilla=loader.get_template("listardisponibles.html")
    contexto={
        'disponibles':disponibles,
    }

    #titulo="Mis Perris | Lista Disponibles" #
    return HttpResponse(plantilla.render(contexto,request))


def listartodos(request):
    titulo="Mis Perris | Lista Todos"
    return render(request,"listartodos.html",{'titulo':titulo})