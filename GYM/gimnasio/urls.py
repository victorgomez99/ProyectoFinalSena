"""GYM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'gimnasio'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'), 
    path('register/', views.registro_Usuario, name='register'),

    path('', views.index, name='index'),
    path('clases/', views.clases, name='clases'),
    path('planes/', views.planes, name='planes'),
    path('inisiosesion/', views.inisiosesion, name='inisiosesion'),
    path('registro/', views.registro, name='registro'),
    path('volver/', views.registro, name='volver'),

    # PRODUCTO
    path('producto/', views.producto, name='producto'),
    path('guardar-producto/', views.guardarProducto, name='guardar-producto'),
    path('producto-formulario/', views.productoFormulario, name='producto-formulario'),
    path('eliminar-producto/<int:id>/', views.eliminarProducto, name='eliminar-producto'),
    path('actualizar-producto/<int:id>/', views.productoFormularioActualizar, name='actualizar-producto'),
    path('editar-producto/', views.editarProducto, name='editar-producto'),

    # PROVEEDOR 
    path('proveedor/', views.proveedor, name='proveedor'),
    path('guardar-proveedor/', views.guardarProveedor, name='guardar-proveedor'),
    path('proveedor-formulario/', views.proveedorFormulario, name='proveedor-formulario'),
    path('eliminar-proveedor/<int:id>/', views.eliminarProveedor, name='eliminar-proveedor'), 
    path('actualizar-proveedor/<int:id>/', views.proveedorFormularioActualizar, name='actualizar-proveedor'),
    path('editar-proveedor/', views.editarProveedor, name='editar-proveedor'),

    # USUARIO
    path('usuario/', views.usuario, name='usuario'),
    path('guardar-usuario/', views.guardarUsuario, name='guardar-usuario'),
    path('usuario-formulario/', views.usuarioFormulario, name='usuario-formulario'),
    path('eliminar-usuario/<int:id>/', views.eliminarUsuario, name='eliminar-usuario'),
    path('actualizar-usuario/<int:id>/', views.usuarioFormularioActualizar, name='actualizar-usuario'),
    path('editar-usuario/', views.editarUsuario, name='editar-usuario'),

    # INVENTARIO  
    path('inventario/', views.inventario, name='inventario'),
    path('guardar-inventario/', views.guardarInventario, name='guardar-inventario'),
    path('inventario-formulario/', views.inventarioFormulario, name='inventario-formulario'),
    path('eliminar-inventario/<int:id>/', views.eliminarInventario, name='eliminar-inventario'),
    path('actualizar-inventario/<int:id>/', views.inventarioFormularioActualizar, name='actualizar-inventario'),
    path('editar-inventario/', views.editarInventario, name='editar-inventario'),

    # VENTA
    path('venta/', views.venta, name='venta'),
    path('guardar-venta/', views.guardarVenta, name='guardar-venta'),
    path('venta-formulario/', views.ventaFormulario, name='venta-formulario'), 
    path('eliminar-venta/<int:id>/', views.eliminarVenta, name='eliminar-venta'),
    path('actualizar-venta/<int:id>/', views.ventaFormularioActualizar, name='actualizar-venta'),
    path('editar-venta/', views.editarVenta, name='editar-venta'),
       
    # ACTIVIDAD 
    path('actividad/', views.actividad, name='actividad'),
    path('guardar-actividad/', views.guardarActividad, name='guardar-actividad'), 
    path('actividad-formulario/', views.actividadFormulario, name='actividad-formulario'), 
    path('eliminar-actividad/<int:id>/', views.eliminarActividad, name='eliminar-actividad'),
    path('actualizar-actividad/<int:id>/', views.actividadFormularioActualizar, name='actualizar-actividad'), 
    path('editar-actividad/', views.editarActividad, name='editar-actividad'), 

    # NOVEDAD 
    path('novedad/', views.novedad, name='novedad'),
    path('guardar-novedad/', views.guardarNovedad, name='guardar-novedad'), 
    path('novedad-formulario/', views.novedadFormulario, name='novedad-formulario'), 
    path('eliminar-novedad/<int:id>/', views.eliminarNovedad, name='eliminar-novedad'),
    path('actualizar-novedad/<int:id>/', views.novedadFormularioActualizar, name='actualizar-novedad'), 
    path('editar-novedad/', views.editarNovedad, name='editar-novedad'),  
     
]

