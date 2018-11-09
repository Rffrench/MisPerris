from django import forms


perfiles=( #perfiles de usuario para el formulario
    ('Administrador','Administrador'),
    ('Adoptante','Adoptante'),
)

estados=( #estados de las mascotas
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'),
    ('Adoptado','Adoptado'),
)


class RegistrarUsuario(forms.Form): #form para registrar el usuario
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    nombreCompleto=forms.CharField(widget=forms.TextInput(),label="Nombre Completo")
    direccionUsuario=forms.CharField(widget=forms.TextInput(),label="Dirección")
    perfil=forms.ChoiceField(choices=perfiles)

class LoginLog(forms.Form): #form para iniciar sesión
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")


class AgregarRescatado(forms.Form): #form para agregar a un rescatado
    #idRescatado=forms.IntegerField(widget=forms.HiddenInput())
    fotoRescatado=forms.ImageField(widget=forms.FileInput(),label="Foto Rescatado")
    nombreRescatado=forms.CharField(widget=forms.TextInput(),label="Nombre Rescatado")
    razaRescatado=forms.CharField(widget=forms.TextInput(),label="Raza Rescatado")
    descripcionRescatado=forms.CharField(widget=forms.TextInput(),label="Descripción")
    estadoRescatado=forms.ChoiceField(choices=estados)
    