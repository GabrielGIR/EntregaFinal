from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .decorators import *



def inicio(request):
    avatar = getavatar(request)
    pedidos = Ordenar.objects.all()
    usuarios = User.objects.all()  # Obtener todos los usuarios registrados(no clientes ya que los usuarios estan relacionados con los usuarios)

    context = {'pedidos': pedidos, 'usuarios': usuarios, 'avatar': avatar}
    return render(request, 'Roel/inicio.html', context)


def cliente(request):
    clientes = Cliente.objects.all()[:5]  # Limitamos a solo 5 clientes
    avatar = getavatar(request)
    clientes_totales = Cliente.objects.count()  # Obtenemos la cantidad total de clientes

    show_ver_mas = False
    if clientes_totales > 5 and not request.user.is_staff:
        show_ver_mas = True  # Mostrar el botón "Ver más" solo si hay más de 5 clientes y el usuario no es administrador

    context = {
        "avatar": avatar,
        "clientes": clientes,
        "show_ver_mas": show_ver_mas,
    }
    return render(request, 'Roel/cliente.html', context)

def distri(request):
    avatar = getavatar(request)
    distribuidoras = Distribuidora.objects.all()
    return render(request, 'Roel/distribuidoras/distri.html', {"avatar": avatar, "distribuidoras": distribuidoras})


def productos_distribuidora(request, distribuidora_id):
    distribuidora = get_object_or_404(Distribuidora, id=distribuidora_id)
    productos = distribuidora.producto_set.all()
    return render(request, 'Roel/distribuidoras/productos_distribuidora.html', {'distribuidora': distribuidora, 'productos': productos})


@login_required
def setDistri(request):
    if request.method == 'POST':
        form = FormSolicitudDistribuidora(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.user = request.user
            solicitud.save()
            mensaje = "¡Gracias por enviar tu solicitud! Pronto nos pondremos en contacto contigo para confirmar si ha sido aprobada o no."
            return redirect('ver_solicitudes_distri')
    else:
        form = FormSolicitudDistribuidora()
    
    return render(request, 'Roel/distribuidoras/setDistri.html', {'form': form})

@login_required
def solicitud_enviada(request):
    return render(request, 'Roel/distribuidoras/solicitud_enviada.html')

@login_required
@allowed_users(allowed_roles=['admin'])
def ver_solicitudes_distri(request):
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        aprobada = request.POST.get('aprobada')
        if solicitud_id and aprobada in ['True', 'False']:
            solicitud = SolicitudDistribuidora.objects.get(id=solicitud_id)
            solicitud.aprobado = aprobada == 'True'
            solicitud.save()

    solicitudes = SolicitudDistribuidora.objects.filter(aprobado=False)  # Obtiene todas las solicitudes pendientes

    context = {
        'solicitudes': solicitudes,
    }

    return render(request, 'Roel/distribuidoras/ver_solicitudes_distri.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def aprobar_solicitud(request, solicitud_id):
    solicitud = SolicitudDistribuidora.objects.get(id=solicitud_id)
    solicitud.aprobado = True
    solicitud.save()

    # Crear una nueva instancia de Distribuidora con los datos de la solicitud aprobada
    distribuidora = Distribuidora(nombre=solicitud.nombre, email=solicitud.email, profesion=solicitud.profesion)
    distribuidora.save()

    return redirect('ver_solicitudes_distri')

@login_required
def local(request):
    avatar = getavatar(request)
    return render(request, 'Roel/local.html',{"avatar":avatar})

@login_required
def setCliente(request):
 #   if request.method == 'POST':
 #       miFormulario = formSetCliente(request.POST)
  #      if miFormulario.is_valid():
  #          data = miFormulario.cleaned_data
   #         cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
   #         cliente.save()
   #         return render(request, "Roel/cliente.html", {"miFormulario": miFormulario, "Cliente": Cliente, "mensaje": "Cliente registrado exitosamente!"})
  #  else:
   #     miFormulario = formSetCliente()

    clientes = Cliente.objects.all()[:5]  # Limitamos a solo 5 clientes
    avatar = getavatar(request)
    clientes_totales = Cliente.objects.count()  # Obtenemos la cantidad total de clientes

    show_ver_mas = False
    if clientes_totales > 5 and not request.user.is_staff:
       show_ver_mas = True  # Mostrar el botón "Ver más" solo si hay más de 5 clientes y el usuario no es administrador

    context = {
        "avatar": avatar,
        "clientes": clientes,
        "show_ver_mas": show_ver_mas,
    }
    return render(request, 'Roel/cliente.html', context)


@login_required
def getCliente(request):
    return render(request, "Roel/getCliente.html")


@login_required
def buscarCliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Cliente.objects.filter(nombre = nombre)
        return render(request, "Roel/getCliente.html", {"clientes":clientes})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)




@login_required
def getDistri(request):
    return render(request, "Roel/getDistri.html")


@login_required
def buscarDistri(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        distribuidoras = Distribuidora.objects.filter(nombre = nombre)
        return render(request, "Roel/getDistri.html", {"distribuidora":distribuidoras})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@login_required
def setLocal(request):
    if request.method == 'POST':
        miFormulario = formSetLocal(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            local = Local(nombre=data["nombre"],calle=data["calle"], pais=data["pais"])
            local.save()
            return render(request, "Roel/setLocal.html", {"miFormulario": miFormulario, "Local": Local})
    else:
        miFormulario = formSetCliente()
    return render(request, "Roel/setLocal.html", {"miFormulario": miFormulario, "Cliente": Local})

@login_required
def getLocal(request):
    return render(request, 'Roel/getLocal.html')

@login_required
def buscarLocal(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        locales = Local.objects.filter(nombre = nombre)
        return render(request, "Roel/getLocal.html", {"local":locales})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)


def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
        else:
            return render(request, 'Roel/registration/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'Roel/registration/login.html')

def registro(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='clientes')
            user.groups.add(group)

            cliente = Cliente.objects.create(user=user)

            return redirect('login')
        else:
            return render(request, 'Roel/registration/register.html')
    else:
        return render(request, 'Roel/registration/register.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['clientes', 'admin'])
def perfilview(request):
    pedidos = Ordenar.objects.filter(cliente=request.user.cliente)  # Filtrar los pedidos del usuario actual
    avatar = getavatar(request)

    context = {'pedidos': pedidos, 'avatar': avatar}
    return render(request, 'Roel/Perfil/perfil.html', context)

@login_required
def editarPerfil(request):
    ordernes = request.user.cliente.orden
    usuario = request.user
    user_basic_data = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance= usuario)
        if form.is_valid():
            user_basic_data.username = form.cleaned_data.get('username')
            user_basic_data.email = form.cleaned_data.get('email')
            user_basic_data.first_name = form.cleaned_data.get('first_name')
            user_basic_data.last_name = form.cleaned_data.get('last_name')
            user_basic_data.save()
            return render(request, 'Roel/Perfil/Perfil.html', {"form":form})
    else:
        form = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'Roel/Perfil/editarPerfil.html', {"form":form})
    
@login_required
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
            form = ChangePasswordForm(data =request.POST ,user= usuario)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return render(request, "Roel/Perfil/Perfil.html")
    else:
            form = ChangePasswordForm(user=usuario)
            return render(request, "Roel/Perfil/changePassword.html", {"form":form})
    
@login_required
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "Roel/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "Roel/Perfil/avatar.html", {'form': form})

@login_required
def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar


@login_required
def setOrden(request):
    if request.method == 'POST':
        form = formSetOrden(request.POST, initial={'cliente': request.user.cliente})
        if form.is_valid():
            form.save()
            return redirect('inicio')

    else:
        form = formSetOrden(initial={'cliente': request.user.cliente})

    context = {'form': form}
    return render(request, 'Roel/crudPedidos/setOrden.html', context)

@login_required
def updateOrden(request, id_orden):

    orden = Ordenar.objects.get(id = id_orden)
    form = formSetOrden(instance = orden)
    if request.method == 'POST':
        form = formSetOrden(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('Roel/inicio.html')

    context = {'form':form}
    return render (request, 'Roel/crudPedidos/setOrden.html', context)  

@login_required
def deleteOrden(request, id_orden):

    orden = Ordenar.objects.get(id = id_orden)
    if request.method == 'POST':
        orden.delete()
        return redirect('Roel/inicio.html')
    context = {'orden':orden}
    return render (request, 'Roel/crudPedidos/deleteOrden.html', context)

@login_required
def foro(request):
    posts = Post.objects.all()
    context = {'post':post}
    return render(render, 'Roel/foro/foro.html')



@login_required
def post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('foro')
    else:
        post_form = PostForm()
    
    return render(request, 'Roel/foro/post.html', {'post_form': post_form})

@login_required
def foro(request):
    avatar = getavatar(request)
    posts = Post.objects.all()
    context = {'posts':posts, "avatar":avatar}
    return render(request,'Roel/foro/foro.html', context )

def aboutme(request):
    return render(request, "Roel/index2.html")

@login_required
@allowed_users(allowed_roles=['admin'])  # Ajusta el rol adecuado para el administrador
def verMasClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Roel/Perfil/VerMasClientes.html', {'clientes': clientes})