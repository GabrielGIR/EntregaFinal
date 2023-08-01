from django.urls import path
from Roel.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', loginWeb),
    path('inicio/', inicio, name="inicio"),
    path('cliente/', cliente, name="cliente"),
    path('distri/', distri, name="distri"),
    path('local/', local, name="local"),
    path('setCliente', setCliente, name="setCliente"),
    path('getCliente',getCliente, name="getCliente"),
    path('buscarCliente',buscarCliente, name="buscarCliente"),
    path('setDistri',setDistri, name="setDistri"),
    path('getDistri',getDistri, name="getDistri"),
    path('setLocal',setLocal, name="setLocal"),
    path('getLocal',getLocal, name="getLocal"),
    path('buscarLocal',buscarLocal, name="buscarLocal"),
    path('iniciar/',loginWeb, name="login"),
    path('registro/',registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name = 'Roel/registration/login.html/'), name="Logout"),
    path('perfil', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword , name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar , name="Avatar"),
    path('setOrden/', setOrden, name='setOrden'),
    path('updateOrden/<str:id_orden>', updateOrden, name='updateOrden'),
    path('deleteOrden/<str:id_orden>', deleteOrden, name='deleteOrden'),
    path('post/', post, name='post'),
    path('foro/', foro, name='foro'),
    path('aboutme/', aboutme, name='aboutme'),
    path('productos_distribuidora/<int:distribuidora_id>/', productos_distribuidora, name='productos_distribuidora'),
    path('ver_solicitudes_distri/', ver_solicitudes_distri, name='ver_solicitudes_distri'),
    path('aprobar_solicitud/<int:solicitud_id>/', aprobar_solicitud, name='aprobar_solicitud'),
 
]
