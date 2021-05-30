from django.contrib import admin

# Register your models here.
from .models import Proveedor,Inventario,Producto,Tipo_Documento,Tipo_Usuario,Usuario,Novedad,UsuarioxNovedad,Actividad,UsuarioxActividad,Venta,VentaxProducto,Factura, registroUsuario

class registroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'contrasena', 'rol')

admin.site.register(registroUsuario, registroUsuarioAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'direccion', 'telefono', 'correo')

admin.site.register(Proveedor, ProveedorAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'cantidad', 'valor_compra', 'fecha_vencimiento', 'proveedor')

admin.site.register(Inventario, InventarioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'valor_venta', 'inventario')


admin.site.register(Producto, ProductoAdmin)

class Tipo_DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_tipoDocumento', 'nombre')

admin.site.register(Tipo_Documento, Tipo_DocumentoAdmin)

class Tipo_UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_tipoUsuario', 'nombre')

admin.site.register(Tipo_Usuario, Tipo_UsuarioAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_Usuario', 'documento', 'num_documento', 'nombre_usuario', 'apellido_usuario', 'direccion', 'telefono', 'correo', 'tipo_usuario')

admin.site.register(Usuario, UsuarioAdmin)

class NovedadAdmin(admin.ModelAdmin):
    list_display = ('id_novedad', 'tipo_novedad', 'nombre_novedad', 'desc_novedad', 'fecha')

admin.site.register(Novedad, NovedadAdmin)

class UsuarioxNovedadAdmin(admin.ModelAdmin):
    list_display = ('id_usuarioxNovedad', 'id_Usuario', 'id_novedad')

admin.site.register(UsuarioxNovedad, UsuarioxNovedadAdmin)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id_actividad', 'nombre_actividad', 'horario', 'desc_actividad')

admin.site.register(Actividad, ActividadAdmin)

class UsuarioxActividadAdmin(admin.ModelAdmin):
    list_display = ('id_usuarioxActividad', 'id_Usuario', 'id_actividad')

admin.site.register(UsuarioxActividad, UsuarioxActividadAdmin)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'tipo_venta', 'desc_venta', 'fecha', 'oferta_vigente', 'valor_venta', 'id_Usuario')

admin.site.register(Venta, VentaAdmin)

class VentaxProductoAdmin(admin.ModelAdmin):
    list_display = ('id_ventaxProducto', 'id_venta', 'id_producto')

admin.site.register(VentaxProducto, VentaxProductoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'valor_pagar', 'descri_factura')

admin.site.register(Factura, FacturaAdmin)
