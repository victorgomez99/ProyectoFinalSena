from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.nombre)

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cantidad = models.SmallIntegerField(null=False, blank=False, unique=False)
    valor_compra = models.IntegerField(null=False, blank=False)
    fecha_vencimiento = models.DateField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.DO_NOTHING)

    def __str__(self):
        return str(self.id_inventario)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=254)
    valor_venta = models.IntegerField(null=False, blank=False)
    inventario = models.ForeignKey(Inventario, on_delete = models.DO_NOTHING)

class Tipo_Documento(models.Model):
    id_tipoDocumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=254)

    def __str__(self):
        return str(self.nombre)
        
class Tipo_Usuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=254)

    def __str__(self):
        return str(self.nombre)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Tipo_Documento, on_delete = models.DO_NOTHING)
    num_documento = models.IntegerField(null=False, blank=False, unique=True)
    nombre_usuario = models.CharField(max_length=254)
    apellido_usuario = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=15, unique=True)
    correo = models.EmailField(max_length=200, unique=True)
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete = models.DO_NOTHING)

    def __str__(self):
        return str(self.nombre_usuario)

class Novedad(models.Model):
    id_novedad = models.AutoField(primary_key=True)
    tipo_novedad = models.CharField(max_length=254)
    nombre_novedad = models.CharField(max_length=254)
    desc_novedad = models.CharField(max_length=254)
    fecha = models.DateField(auto_now_add=True)

class UsuarioxNovedad(models.Model):
    id_usuarioxNovedad = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    id_novedad = models.ForeignKey(Novedad, on_delete = models.DO_NOTHING)

class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=254)
    horario = models.DateTimeField(auto_now_add=False)
    desc_actividad = models.CharField(max_length=254)

class UsuarioxActividad(models.Model):
    id_usuarioxActividad = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    id_actividad = models.ForeignKey(Actividad, on_delete = models.DO_NOTHING)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    tipo_venta = models.CharField(max_length=254)
    desc_venta = models.CharField(max_length=254)
    fecha = models.DateField(auto_now_add=True)
    oferta_vigente = models.CharField(max_length=254)
    valor_venta = models.IntegerField(null=False, blank=False)
    id_Usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)

class VentaxProducto(models.Model):
    id_ventaxProducto = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete = models.DO_NOTHING)
    id_producto = models.ForeignKey(Producto, on_delete = models.DO_NOTHING)

class Factura(models.Model):
    id_factura = models.OneToOneField(Venta, on_delete = models.DO_NOTHING)
    valor_pagar = models.IntegerField(null=False, blank=False)
    descri_factura = models.CharField(max_length=254)

class registroUsuario(models.Model):
    ROL = (
        (1, 'Administrador'),
        (2, 'Empleado'),
        (3, 'Usuario'),
    )
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200, unique=True)
    contrasena = models.CharField(max_length=200, unique=True)
    rol = models.IntegerField(choices=ROL, default=3)
    
    def __str__(self):
        return str(self.rol)
    
