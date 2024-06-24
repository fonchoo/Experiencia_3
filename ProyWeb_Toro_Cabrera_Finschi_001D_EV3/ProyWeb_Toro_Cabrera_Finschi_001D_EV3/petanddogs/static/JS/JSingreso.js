var email = document.getElementById('mail');
var contraseña = document.getElementById('contraseña');
var errorContraseña = document.getElementById('errorContraseña');
var mensajeExito = document.getElementById('mensajeExito');


function enviarFormulario(){
    var hayErrores = false;

    var mensajesError = [];

    //validacion nombre

    //validacion apellido

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
        errorContraseña.textContent = 'Ingresa la contraseña correcta';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorContraseña.textContent = '';
    }

    //validacion confirmacio de contraseña

    if(hayErrores){
        return false;
    } else{
        return true;
    }
}
