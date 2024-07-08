from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/FormRegistro', views.formRegistro, name='FormRegistro'),
    path('index/perfil', views.perfil, name='perfil'),
    path('login/',views.login_view, name='login_view'),
    path('index/quienessomos', views.quiensessomos, name='quienessomos'),
    path('index/galeria', views.galeria, name='galeria'),
    path('index/adopcion', views.adopcion, name='adopcion'),
    path('index/razas', views.razas, name='razas'),
    path('quienessomos/formContacto', views.formContacto, name='formContacto'),
    path('galeria/calculadora', views.calculadora, name='calculadora'),
    path('galeria/lindocat', views.lindoCat, name='lindocat'),
    path('galeria/acana', views.acana, name='acana'),
    path('galeria/naturea', views.naturea, name='naturea'),
    path('galeria/diamond', views.diamond, name='diamond'),
    path('galeria/orijen', views.orijen, name='orijen'),
    path('galeria/taste', views.taste, name='taste'),
    path('crud',views.crud,name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('logout/',views.exit, name='exit'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('registrosAdd', views.registroAdd, name='registroAdd'),
    path('agregar_al_carrito/<str:producto_id>', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('mostrar_carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('validar_compra/', views.validar_compra, name='validar_compra'),
]

