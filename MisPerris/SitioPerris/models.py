from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Usuario(models.Model):
#    username=models.CharField(primary_key=True, max_length=20)
#    password=models.CharField(max_length=20)
#    correo=models.EmailField(max_length=30)
#    nombreCompleto=models.CharField(max_length=30)
#    direccionUsuario=models.CharField(max_length=30)
#    tipoUsuario=models.IntegerField(default=1)#por defecto usr normal(1). (2) es admin

class Usuario(models.Model): #clase para el usuario 
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #username=models.CharField(primary_key=True, max_length=20)
    #password=models.CharField(max_length=20)
    correo=models.EmailField(max_length=30)
    nombreCompleto=models.CharField(max_length=30)
    direccionUsuario=models.CharField(max_length=30)
    perfil=models.CharField(max_length=20,default="Adoptante")

class Rescatado(models.Model): #clase para los rescatados
    idRescatado=models.AutoField(primary_key=True)
    fotoRescatado=models.ImageField(upload_to="fotos_rescatados")
    nombreRescatado=models.CharField(max_length=20)
    razaRescatado=models.CharField(max_length=20)
    descripcionRescatado=models.TextField(max_length=80)
    estadoRescatado=models.CharField(max_length=20,default="Rescatado")
