var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var email = document.getElementById('mail');
var contraseña = document.getElementById('contraseña');
var confContraseña = document.getElementById('confirmContraseña');
var errorNombre = document.getElementById('errorNombre');
var errorApellido = document.getElementById('errorApellido');
var errorMail = document.getElementById('errorMail');
var errorContraseña = document.getElementById('errorContraseña');
var errorConfContraseña = document.getElementById('errorContraseña2');
var mensajeExito = document.getElementById('mensajeExito');


function enviarFormulario(){
    var hayErrores = false;

    var mensajesError = [];

    //validacion nombre
    if(nombre.value.trim() === ''){
        mensajesError.push('Ingrese su nombre');
        errorNombre.textContent = 'Ingrese su nombre';
        hayErrores = true;
        console.log('Nombre validado')
    } else if (!/^[A-Za-záéíóúÁÉÍÓÚñÑ]+$/.test(nombre.value)){
        mensajesError.push('El nombre solo puede contener letras');
        errorNombre.textContent = 'El nombre solo puede contener letras';
        hayErrores = true;
        console.log('Nombre validado')
    } else{
        errorNombre.textContent ='';
    }

    //validacion apellido
    if(apellido.value.trim() === ''){
        mensajesError.push('Ingrese su apelldio');
        errorApellido.textContent = 'Ingrese su apellido';
        hayErrores = true;
        console.log('apellido validado')
    } else if (!/^[A-Za-záéíóúÁÉÍÓÚñÑ]+$/.test(apellido.value)){
        mensajesError.push('El apellido solo puede contener letras');
        errorApellido.textContent = 'El apellido solo puede contener letras';
        hayErrores = true;
        console.log('apellido validado')
    } else{
        errorApellido.textContent ='';
    }

    //validacion email
    if(email.value.trim() === '') {
        mensajesError.push('Ingresa tu correo');
        errorMail.textContent = 'Ingresa tu correo';
        hayErrores = true; // Se establece a true si hay un error
    } else if (!/\S+@\S+\.\S+/.test(email.value)) {
        mensajesError.push('El correo electrónico debe tener un formato válido');
        errorMail.textContent = 'El correo electrónico debe tener un formato válido';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorMail.textContent = '';
    }

    //validacion contraseña
    if(contraseña.value.trim() === '') {
        errorContraseña.textContent = 'Ingresa una contraseña';
        hayErrores = true; // Se establece a true si hay un error
    } else if (contraseña.value.length < 4) {
        errorContraseña.textContent = 'La contraseña debe tener minimo 4';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorContraseña.textContent = '';
    }

    //validacion confirmacio de contraseña
    if(confContraseña.value.trim() === '') {
        errorConfContraseña.textContent = 'Repite tu contraseña';
        hayErrores = true; // Se establece a true si hay un error
    } else if (confContraseña.value !== contraseña.value) {
        errorConfContraseña.textContent = 'Las contraseñas no coinciden';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorConfContraseña.textContent = '';
    }

    if(hayErrores){
        return false;
    } else{
        return true;
    }
}