from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.db import IntegrityError
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Inventario, Producto, Tipo_Documento, Usuario, Tipo_Usuario, Proveedor, Venta, Actividad, Novedad, registroUsuario

def index(request):
    return render(request, 'gimnasio/index.html')

def clases(request):
    return render(request, 'gimnasio/clases.html')

def planes(request):
    return render(request, 'gimnasio/planes.html')

def inisiosesion(request):
    return render(request, 'gimnasio/inisiosesion.html')

def registro(request):
    return render(request, 'gimnasio/registro.html')

################    LOGIN    ##############
def login(request):
    try:
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        q = registroUsuario.objects.get(correo = correo, contrasena = contrasena)
        request.session["login"] = [
            q.id, 
            q.correo, 
            q.rol
        ]

        return HttpResponseRedirect(reverse('gimnasio:index')) 
    except:
        return HttpResponseRedirect(reverse('gimnasio:index'))

def logout(request):
    try:
        del request.session["login"]
        return HttpResponseRedirect(reverse('gimnasio:index', args=()))  
    except:
        return HttpResponse("Ocurrió un error, intente de nuevo.")

def registro_Usuario(request):
    if request.method=="POST":
        if request.POST['contrasena'] == request.POST['contrasena2']:
            q = registroUsuario(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                correo=request.POST['correo'],
                contrasena=request.POST['contrasena'],
                #rol=request.POST['rol']
            )
            q.save()
            messages.success(request, "Inició sesión correctamente!") 
            return HttpResponseRedirect(reverse('gimnasio:index'))
        else:
            return HttpResponse("Claves no concuerdan...")    
    else:
        return HttpResponse("fin")


################    NOVEDAD    ##############
def novedad(request):
    q = Novedad.objects.all()
    
    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/novedad.html', contexto)

def novedadFormulario(request):
    return render(request, 'gimnasio/novedad-formulario.html')

def guardarNovedad(request):
    try:
        if request.method == "POST":
            tipnove = request.POST["tipo_novedad"]
            nomnove = request.POST["nombre_novedad"]
            descnove = request.POST["desc_novedad"]
            fech = request.POST["fecha"]

            q = Novedad(tipo_novedad = tipnove, nombre_novedad = nomnove, desc_novedad = descnove, fecha = fech )
            q.save()
            messages.success(request, "Novedad guardada correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe una con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:novedad', args=())) 

def eliminarNovedad(request, id):
    try:
        q = Novedad.objects.get(pk = id) 
        aux = q.id_novedad
        q.delete()
        messages.success(request, "Novedad eliminada correctamente! -> " + str(aux))
    except Novedad.DoesNotExist:
        messages.error(request, "Error: No se encontró la Novedad. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen las Novedades.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:novedad', args=()))

def novedadFormularioActualizar(request, id):
    try:
        q = Novedad.objects.get(pk = id)
        contexto = { 'novedad': q }
        messages.success(request, "Novedad actualizada correctamente! -> " )
    except Novedad.DoesNotExist:
        messages.error(request, "Error: No se encontró la Novedad. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen las Novedades.")

    return render(request, 'gimnasio/actualizar-formu-novedad.html', contexto)

def editarNovedad(request):
    if request.method == "POST":
        id = request.POST['id']
        tipnove = request.POST["tipo_novedad"]
        nomnove = request.POST["nombre_novedad"]
        descnove = request.POST["desc_novedad"]
        fech = request.POST["fecha"]

        q = Novedad.objects.get(pk=id)
        q.tipo_novedad = tipnove
        q.nombre_novedad = nomnove
        q.desc_novedad = descnove
        q.fecha = fech 
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:novedad', args=()))
    else:
        return HttpResponse("fin")

################    PRODUCTO    ##############
def actividad(request):
    q = Actividad.objects.all()
   
    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/actividad.html', contexto)

def actividadFormulario(request):
    return render(request, 'gimnasio/actividad-formulario.html')

def guardarActividad(request):
    try:
        if request.method == "POST":
            nom = request.POST["nombre_actividad"]
            hora = request.POST["horario"]
            desacti = request.POST["desc_actividad"]
            
            q = Actividad(nombre_actividad = nom, horario = hora, desc_actividad = desacti)
            q.save()
            messages.success(request, "Actividad guardada correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe la Actividad con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:actividad', args=()))   

def eliminarActividad(request, id):
    try:
        q = Actividad.objects.get(pk = id) 
        aux = q.id_actividad
        q.delete()
        messages.success(request, "Actividad eliminada correctamente! -> " + str(aux))
    except Actividad.DoesNotExist:
        messages.error(request, "Error: No se encontró la Actividad. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen las Actividades.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:actividad', args=()))

def actividadFormularioActualizar(request, id):
    try:
        q = Actividad.objects.get(pk = id)
        contexto = { 'actividad': q }
        messages.success(request, "Actividad actualizada correctamente! -> " )
    except Actividad.DoesNotExist:
        messages.error(request, "Error: No se encontró la Actividad. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen las Actividades.")

    return render(request, 'gimnasio/actualizar-formu-actividad.html', contexto)

def editarActividad(request):
    if request.method == "POST":
        id = request.POST['id']
        nom = request.POST["nombre_actividad"]
        hora = request.POST["horario"]
        desact = request.POST["desc_actividad"]

        q = Actividad.objects.get(pk=id)
        q.nombre_actividad = nom
        q.horario = hora
        q.desc_actividad = desact
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:actividad', args=()))
    else:
        return HttpResponse("fin")

################    PRODUCTO    ##############
def producto(request):
    q = Producto.objects.all()
    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/producto.html', contexto)

def productoFormulario(request):
    q = Inventario.objects.all()
    contexto = {"inventarios":q}
 
    return render(request, 'gimnasio/producto-formulario.html', contexto)

def guardarProducto(request):
    try:
        if request.method == "POST":
            nom = request.POST["nombre"]
            valoventa = request.POST["valor_venta"]
            inven = Inventario.objects.get(id_inventario = request.POST["inventario"])

            q = Producto(nombre = nom, valor_venta = valoventa, inventario = inven )
            q.save()
            messages.success(request, "Producto guardado correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe un Producto con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:producto', args=()))   

def eliminarProducto(request, id):
    try:
        q = Producto.objects.get(pk = id) 
        aux = q.id_producto
        q.delete()
        messages.success(request, "Producto eliminado correctamente! -> " + str(aux))
    except Usuario.DoesNotExist:
        messages.error(request, "Error: No se encontró el Producto. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen los Productos.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:producto', args=()))

def productoFormularioActualizar(request, id):
    try:
        q = Producto.objects.get(pk = id)
        contexto = { 'producto': q }
        messages.success(request, "Producto actualizado correctamente! -> " )
    except Producto.DoesNotExist:
        messages.error(request, "Error: No se encontró el Producto. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen los Productos.")

    return render(request, 'gimnasio/actualizar-formu-producto.html', contexto)

def editarProducto(request):
    if request.method == "POST":
        id = request.POST['id']
        nom = request.POST["nombre"]
        valoventa = request.POST["valor_venta"]
        inven = Inventario.objects.get(id_inventario = request.POST["inventario"])
        
        q = Producto.objects.get(pk=id) 
        q.nombre = nom
        q.valor_venta = valoventa
        q.inventario = inven
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:producto', args=()))
    else:
        return HttpResponse("fin")

################    PROVEEDOR    ##############
def proveedor(request):
    q = Proveedor.objects.all()

    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    return render(request, 'gimnasio/proveedor.html', contexto)

def proveedorFormulario(request):
    return render(request, 'gimnasio/proveedor-formulario.html')

def guardarProveedor(request):
    try:
        if request.method == "POST":
            nom = request.POST["nombre"]
            dire = request.POST["direccion"]
            tel = request.POST["telefono"]
            corr = request.POST["correo"]

            q = Proveedor(nombre = nom, direccion = dire, telefono = tel, correo = corr )
            q.save()
            messages.success(request, "Proveedor guardado correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe un Proveedor con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:proveedor', args=()))   

def eliminarProveedor(request, id):
    try:
        q = Proveedor.objects.get(pk = id) 
        aux = q.id_proveedor
        q.delete()
        messages.success(request, "Proveedor eliminado correctamente! -> " + str(aux))
    except Proveedor.DoesNotExist:
        messages.error(request, "Error: No se encontró el Proveedor. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen los Proveedores.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:proveedor', args=()))

def proveedorFormularioActualizar(request, id):
    try:
        q = Proveedor.objects.get(pk = id)
        contexto = { 'proveedor': q }
        messages.success(request, "Proveedor actualizado correctamente! -> " )
    except Proveedor.DoesNotExist:
        messages.error(request, "Error: No se encontró el Proveedor. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen los Proveedores.")

    return render(request, 'gimnasio/actualizar-formu-proveedor.html', contexto)

def editarProveedor(request):
    if request.method == "POST":
        id = request.POST['id']
        nom = request.POST["nombre"]
        dire = request.POST["direccion"]
        tel = request.POST["telefono"]
        corr = request.POST["correo"]

        q = Proveedor.objects.get(pk=id)
        q.nombre = nom
        q.direccion = dire
        q.telefono = tel
        q.correo = corr 
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:proveedor', args=()))
    else:
        return HttpResponse("fin")

################    INVENTARIO    ##############
def inventario(request):
    q = Inventario.objects.all()
    
    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/inventario.html', contexto)

def inventarioFormulario(request):
    q = Proveedor.objects.all()
    contexto = {"proveedores":q}
 
    return render(request, 'gimnasio/inventario-formulario.html', contexto)

def guardarInventario(request):
    try:
        if request.method == "POST":
            canti = request.POST["cantidad"]
            valocompra = request.POST["valor_compra"]
            fechvenci = request.POST["fecha_vencimiento"]
            p = Proveedor.objects.get(id_proveedor = request.POST["proveedor"])

            q = Inventario(cantidad = canti, valor_compra = valocompra, fecha_vencimiento = fechvenci, proveedor = p )
            q.save()
            messages.success(request, "Inventario guardado correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe un Inventario con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:inventario', args=()))   

def eliminarInventario(request, id):
    try:
        q = Inventario.objects.get(pk = id) 
        aux = q.id_inventario
        q.delete()
        messages.success(request, "Inventario eliminado correctamente! -> " + str(aux))
    except Inventario.DoesNotExist:
        messages.error(request, "Error: No se encontró el Inventario. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen los Inventarios.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:inventario', args=()))

def inventarioFormularioActualizar(request, id):
    try:
        q = Inventario.objects.get(pk = id)
        contexto = { 'inventario': q }
        messages.success(request, "Inventario actualizado correctamente! -> " )
    except Inventario.DoesNotExist:
        messages.error(request, "Error: No se encontró el Inventario. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen los Inventarios.")

    return render(request, 'gimnasio/actualizar-formu-inventario.html', contexto)

def editarInventario(request):
    if request.method == "POST":
        id = request.POST['id']
        canti = request.POST["cantidad"]
        valocomp = request.POST["valor_compra"]
        fechvenci = request.POST["fecha_vencimiento"]
        provee = Proveedor.objects.get(id_proveedor = request.POST["proveedor"])

        q = Inventario.objects.get(pk=id) 
        q.cantidad = canti
        q.valor_compra = valocomp
        q.fecha_vencimiento = fechvenci
        q.proveedor = provee
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:inventario', args=()))
    else:
        return HttpResponse("fin")

################    VENTAS    ##############
def venta(request):
    q = Venta.objects.all()

    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/venta.html', contexto)

def ventaFormulario(request):
    q = Usuario.objects.all()
    contexto = {"usuarios":q}
 
    return render(request, 'gimnasio/venta-formulario.html', contexto)

def guardarVenta(request):
    try:
        if request.method == "POST":
            tipven = request.POST["tipo_venta"]
            desven = request.POST["desc_venta"]
            fech = request.POST["fecha"]
            ofervigen = request.POST["oferta_vigente"]
            valovent = request.POST["valor_venta"]
            usu = Usuario.objects.get(id_Usuario = request.POST["id_Usuario"])

            q = Venta(tipo_venta = tipven, desc_venta = desven, fecha = fech, oferta_vigente = ofervigen, valor_venta = valovent, id_Usuario = usu )
            q.save()
            messages.success(request, "Venta guardada correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe una venta con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:venta', args=()))

def eliminarVenta(request, id):
    try:
        q = Venta.objects.get(pk = id) 
        aux = q.id_venta
        q.delete()
        messages.success(request, "Venta eliminada correctamente! -> " + str(aux))
    except Venta.DoesNotExist:
        messages.error(request, "Error: No se encontró la Venta. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen las Ventas.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:venta', args=()))

def ventaFormularioActualizar(request, id):
    try:
        q = Venta.objects.get(pk = id)
        contexto = { 'venta': q }
        messages.success(request, "Venta actualizada correctamente! -> " )
    except Usuario.DoesNotExist:
        messages.error(request, "Error: No se encontró la Venta. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen las Ventas.")

    return render(request, 'gimnasio/actualizar-formu-venta.html', contexto)

def editarVenta(request):
    if request.method == "POST":
        id = request.POST['id']
        tipven = request.POST["tipo_venta"]
        desven = request.POST["desc_venta"]
        fech = request.POST["fecha"]
        ofervigen = request.POST["oferta_vigente"]
        valovent = request.POST["valor_venta"]
        usu = Usuario.objects.get(id_Usuario = request.POST["id_Usuario"])

        q = Venta.objects.get(pk=id) 
        q.tipo_venta = tipven
        q.desc_venta = desven
        q.fecha = fech
        q.oferta_vigente = ofervigen
        q.valor_venta = valovent
        q.id_Usuario = usu
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:venta', args=()))
    else:
        return HttpResponse("fin")

################    USUARIO    ##############
def usuario(request):
    q = Usuario.objects.all()

    paginator = Paginator(q, 3) # Mostrar 3 compaías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = { "datos": page_obj }
    
    return render(request, 'gimnasio/usuario.html', contexto)

def usuarioFormulario(request):
    q = Tipo_Documento.objects.all()
    contexto = {"id_tipoDocumento":q}
 
    return render(request, 'gimnasio/usuario-formulario.html', contexto)

def guardarUsuario(request):
    try:
        if request.method == "POST":
            docu = Tipo_Documento.objects.get(id_tipoDocumento = request.POST["id_tipoDocumento"])
            n_docu = request.POST["num_documento"]
            nom = request.POST["nombre_usuario"]
            apell = request.POST["apellido_usuario"]
            dire = request.POST["direccion"]
            tel = request.POST["telefono"]
            corr = request.POST["correo"]
            tipo_usu = Tipo_Usuario.objects.get(id_tipoUsuario = request.POST["tipo_usuario"])

            q = Usuario(documento = docu, num_documento = n_docu, nombre_usuario = nom, apellido_usuario = apell, direccion = dire, telefono = tel, correo = corr, tipo_usuario = tipo_usu )
            q.save()
            messages.success(request, "Usuario guardado correctamente!")
        else:
            messages.warning(request, "<strong>Advertencia</strong>: Usted no envió los datos a través del formulario.")
    except IntegrityError:
        messages.error(request, "Error: Ya existe un usuario con ese NIT.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))
    
    return HttpResponseRedirect(reverse('gimnasio:usuario', args=()))   

def eliminarUsuario(request, id):
    try:
        q = Usuario.objects.get(pk = id) 
        aux = q.id_Usuario
        q.delete()
        messages.success(request, "Usuario eliminado correctamente! -> " + str(aux))
    except Usuario.DoesNotExist:
        messages.error(request, "Error: No se encontró el Usuario. -> " + str(id))
    except IntegrityError:
        messages.error(request, "Error: Existen los usuarios.")
    except Exception as e:
        messages.error(request, "Error: " + str(e))

    return HttpResponseRedirect(reverse('gimnasio:usuario', args=()))

def usuarioFormularioActualizar(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        contexto = { 'usuario': q }
        messages.success(request, "Usuario actualizado correctamente! -> " )
    except Usuario.DoesNotExist:
        messages.error(request, "Error: No se encontró el Usuario. -> ")
    except IntegrityError:
        messages.error(request, "Error: Existen los usuarios.")

    return render(request, 'gimnasio/actualizar-formulario.html', contexto)

def editarUsuario(request):
    if request.method == "POST":
        docu = Tipo_Documento.objects.get(id_tipoDocumento = request.POST["id_tipoDocumento"])
        id = request.POST['id']
        n_docu = request.POST["num_documento"]
        nom = request.POST["nombre_usuario"]
        apell = request.POST["apellido_usuario"]
        dire = request.POST["direccion"]
        tel = request.POST["telefono"]
        corr = request.POST["correo"]
        tipo_usu = Tipo_Usuario.objects.get(id_tipoUsuario = request.POST["tipo_usuario"])

        q = Usuario.objects.get(pk=id) 
        q.documento = docu
        q.num_documento = n_docu
        q.nombre_usuario = nom
        q.apellido_usuario = apell
        q.direccion = dire
        q.telefono = tel
        q.correo = corr
        q.tipo_usuario = tipo_usu
        q.save()    #actualizar
        return HttpResponseRedirect(reverse('gimnasio:usuario', args=()))
    else:
        return HttpResponse("fin")



