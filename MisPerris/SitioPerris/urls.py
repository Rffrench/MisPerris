from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns=[
    url(r'^Inicio/$',views.index,name="inicio"),
    url(r'^$',views.index), #con esto dejo como homepage la pag de inicio
    url(r'^Login/$',views.ingresar,name="login"),
    url(r'^Registro/$',views.registroUsuarios,name="registro"),
    url(r'^salir/$',views.salir,name="salida"),
    url(r'^AgregarRescatado/$',views.agregarrescatado,name="agregarrescatado"),
    url(r'^ListarRescatados/$',views.listarrescatados,name="listarrescatados"),
    url(r'^ListarDisponibles/$',views.listardisponibles,name='listardisponibles'),
    url(r'^ListarTodos/$',views.listartodos,name='listartodos'),
    
    
    url(
    r'^password_reset/$',
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset.html",
        email_template_name="registration/password_reset_email.html",
        #success_url=reverse_lazy('partners:password_reset_done'), # might be required
    ),
    name='password_reset'
),
    
    
] 