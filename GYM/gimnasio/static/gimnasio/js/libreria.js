console.log("Hola desde JS !")

function eliminarUsuario(ruta){
    resultado = confirm("Está seguro de eliminar el usuario? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarProducto(ruta){
    resultado = confirm("Está seguro de eliminar el producto? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarProveedor(ruta){
    resultado = confirm("Está seguro de eliminar el proveedor? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarInventario(ruta){
    resultado = confirm("Está seguro de eliminar el inventario? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarVenta(ruta){
    resultado = confirm("Está seguro de eliminar la Venta? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarActividad(ruta){
    resultado = confirm("Está seguro de eliminar la Actividad? ")
    if(resultado){
        location.href=ruta;
    }
}

function eliminarNovedad(ruta){
    resultado = confirm("Está seguro de eliminar la Novedad? ")
    if(resultado){
        location.href=ruta;
    }
}

function validarPasswordRegistro(){
    p1 = $('#Contraseña').val()
    p2 = $('#Contraseña2').val()

    if (p1 == p2){
        return true;
    }
    else{
        $('#mensaje_modal').html("Las contraseñas no coinciden...");
        $('#exampleModal').modal('show');
        return false;
    }
}

function login(){
    resultado = alert("* Iniciaste sesión correctamente - BIENVENID@ *")
    if(resultado){
        location.href=ruta;
    }
}

function alerta(){
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'Iniciaste sesión correctamente',
        showConfirmButton: false,
        timer: 1500
    });
}

function cerrarsesion(){
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'Cerraste sesión correctamente',
        showConfirmButton: false,
        timer: 1500
    });
}
