from django.shortcuts import render
from .models import Categoria, Producto, BoletaCompra, DetalleCompra
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import UserEditForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProductoSearchForm

from rest_framework import generics
from .models import Produc
from .serializers import ProducSerializer

class ProducCreateView(generics.CreateAPIView):
    queryset = Produc.objects.all()
    serializer_class = ProducSerializer
    
class ProducDetailView(generics.RetrieveAPIView):
    queryset = Produc.objects.all()
    serializer_class = ProducSerializer
    
class ProducListView(generics.ListAPIView):
    queryset = Produc.objects.all()
    serializer_class = ProducSerializer

# Create your views here.
def index(request):
    context={}
    return render(request,'petanddogs/index.html', context)

def formRegistro(request):
    context={}
    return render(request,'registration/register.html', context)

def perfil(request):
    context={}
    return render(request,'petanddogs/perfil.html', context)

def quiensessomos(request):
    context={}
    return render(request,'petanddogs/quienessomos.html', context)

def galeria(request):
    context={}
    return render(request,'petanddogs/galeria.html', context)

def adopcion(request):
    context={}
    return render(request,'petanddogs/adopcion.html', context)

def razas(request):
    context={}
    return render(request, 'petanddogs/razas.html', context)

def formContacto(request):
    context={}
    return render(request, 'petanddogs/formulariocontacto.html', context)

def calculadora(request):
    context={}
    return render(request, 'petanddogs/calculadora.html', context)

@login_required
def lindoCat(request):
    context={}
    return render(request,'petanddogs/LindoCat.html', context)

@login_required
def acana(request):
    context={}
    return render(request, 'petanddogs/Acana.html', context)

@login_required
def naturea(request):
    context={}
    return render(request, 'petanddogs/Naturea.html', context)

@login_required
def diamond(request):
    context={}
    return render(request, 'petanddogs/Diamond.html', context)

@login_required
def orijen(request):
    context={}
    return render(request, 'petanddogs/Orijen.html', context)

@login_required
def taste(request):
    context={}
    return render(request, 'petanddogs/Taste.html', context)
#***************************** CRUD *************************************
@login_required
def crud(request):
    form = ProductoSearchForm()
    query = request.GET.get('query', '')
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    page = request.GET.get('page', 1)
    paginator = Paginator(productos, 10)

    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    context = {
        'productos': productos,
        'paginator': paginator,
        'form': form,
        'query': query
    }
    return render(request, 'petanddogs/product_list.html', context)

@login_required
@permission_required('petanddogs.add_producto')
def productosAdd(request):
    if request.method != "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render(request,'petanddogs/productos_add.html',context)
    else:
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        imagen=request.FILES.get("imagen")
        precio=request.POST["precio"]
        stock=request.POST["stock"]
        categoria=request.POST["categoria"]
        activo="1"       
                
        objCategoria=Categoria.objects.get(idCategoria = categoria)
        obj=Producto.objects.create(id_producto=id,
                                  nombre=nombre,
                                  descripcion=descripcion,
                                  imagen=imagen,
                                  precio=precio,
                                  stock=stock,
                                  categoria=objCategoria,
                                  activo=1)
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request,'petanddogs/productos_add.html',context)
@login_required
@permission_required('petanddogs.delete_producto')
def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)
        
        producto.delete()
        mensaje="Bien, datos eliminados"
        productos= Producto.objects.all()
        context= {'productos': productos, 'mensajes': mensaje}
        return render(request,'petanddogs/product_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        productos= Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'petanddogs/product_list.html',context)
@login_required
def productosUpdate(request):
    if  request.method =="POST":
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        imagen=request.FILES.get("imagen")
        precio=request.POST["precio"]
        stock=request.POST["stock"]
        categoria=request.POST["categoria"]    
        activo="1"   
                
        objCategoria=Categoria.objects.get(idCategoria = categoria)
        
        producto=Producto()
        producto.id_producto=id
        producto.nombre=nombre
        producto.descripcion=descripcion
        if imagen:
            producto.imagen = imagen
        producto.precio=precio
        producto.stock=stock
        producto.categoria=objCategoria
        producto.activo=1
        producto.save()
        
        categorias = Categoria.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'categorias':categorias,'producto':producto}
        return render(request,'petanddogs/productos_edit.html',context)
    else:
        productos= Producto.objects.all()
        context={'productos':productos}
        return render(request, 'petanddogs/product_list.html', context)
    
@login_required
@permission_required('petanddogs.change_producto')
def productos_findEdit(request,pk):
    if pk !="":
       producto=Producto.objects.get(id_producto=pk)
       categorias=Categoria.objects.all()
       
       print(type(producto.categoria))
       
       context={'producto':producto,'categorias':categorias}
       if producto:
           return render(request,'petanddogs/productos_edit.html', context)
       else:
           context={'mensaje':"Error, id no existe..."}
           return render(request, 'petanddogs/product_list.html', context)

#***************************** REGISTRO *************************************
@csrf_protect
def registroAdd(request):
    if request.method == "POST":
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        password=request.POST["password"]
        password_confirm=request.POST["password_confirm"]

        if CustomUser.objects.filter(email=email).exists():
            return render(request,'register.html',{'error_message':'El email ya esta registrado'})
        
        user=CustomUser.objects.create(email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    password=make_password(password))

        user.save()
        login(request, user)
        return redirect('login')
    context={'mensaje' : 'Datos registrados...'}
    return render(request, 'petanddogs/login.html', context)

#***************************** LOGIN *************************************
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('galeria')
            else:
                return render(request, 'registration/login.html', {'error_message': 'Email o contraseña incorrectos'})
        except User.DoesNotExist:
            return render(request,'registration/login.html', {'error_message': 'Email o contraseña incorrectos'})
    return render(request,'registration/login.html')
#***************************** Editar perfil *************************************
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirigir a la vista del perfil después de guardar
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'petanddogs/editar_perfil.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('/')

#***************************** Carro de compra *************************************

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito = request.session.get('carrito', {})
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += cantidad
        else:
            carrito[producto_id] = {
                'nombre': producto.nombre,
                'precio': producto.precio,
                'cantidad': cantidad,
                'imagen': producto.imagen.url if producto.imagen else None
            }
        request.session['carrito'] = carrito
        return redirect('mostrar_carrito')

    return render(request, 'agregar_al_carrito.html', {'producto': producto})

@login_required
def mostrar_carrito(request):
    carrito = request.session.get('carrito', {})
    return render(request, 'petanddogs/mostrar_carrito.html', {'carrito': carrito})

@login_required
def procesar_compra(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        return redirect('mostrar_carrito')

    boleta = BoletaCompra(cliente=request.user, fecha_compra=timezone.now(), estado_pedido='recibido')
    boleta.save()
    
    for producto_id, detalles in carrito.items():
        producto = get_object_or_404(Producto, id_producto=producto_id)
        cantidad = detalles['cantidad']
        precio = detalles['precio']
        detalle = DetalleCompra(boleta=boleta, producto=producto, cantidad=cantidad, precio=precio)
        detalle.save()

    request.session['carrito'] = {}
    return render(request, 'petanddogs/compra_validada.html', {'boleta': boleta})

def lista_compras(request):
    compras = BoletaCompra.objects.all()
    context = {
        'compras': compras
    }
    return render(request, 'petanddogs/lista_compras.html', context)

