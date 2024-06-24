var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var mail = document.getElementById('mail');
var mensaje = document.getElementById('mensaje');
var errorNombre = document.getElementById('errorNombre');
var errorApellido = document.getElementById('errorApellido');
var errorMail = document.getElementById('errorMail');
var errorMensaje = document.getElementById('errorMensaje');
var mensajeExito = document.getElementById('mensajeExito');

function enviarFormulario() {
    console.log('Enviando formulario...')

    var hayErrores = false; // Variable para verificar si hay errores

    var mensajesError = [];

    if(nombre.value.trim() === '') {
        mensajesError.push('Ingresa tu nombre');
        errorNombre.textContent = 'Ingresa tu nombre';
        hayErrores = true; // Se establece a true si hay un error
    } else if (!/^[A-Za-záéíóúÁÉÍÓÚñÑ]+$/.test(nombre.value)) {
        mensajesError.push('El nombre solo puede contener letras');
        errorNombre.textContent = 'El nombre solo puede contener letras';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorNombre.textContent = '';
    }

    if(apellido.value.trim() === '') {
        mensajesError.push('Ingresa tu apellido');
        errorApellido.textContent = 'Ingresa tu apellido';
        hayErrores = true; // Se establece a true si hay un error
    } else if (!/^[A-Za-záéíóúÁÉÍÓÚñÑ]+$/.test(apellido.value)) {
        mensajesError.push('El apellido solo puede contener letras');
        errorApellido.textContent = 'El apellido solo puede contener letras';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorApellido.textContent = '';
    }

    if(mail.value.trim() === '') {
        mensajesError.push('Ingresa tu mail');
        errorMail.textContent = 'Ingresa tu mail';
        hayErrores = true; // Se establece a true si hay un error
    } else if (!/\S+@\S+\.\S+/.test(mail.value)) {
        mensajesError.push('El correo electrónico debe tener un formato válido');
        errorMail.textContent = 'El correo electrónico debe tener un formato válido';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorMail.textContent = '';
    }

    if(mensaje.value.trim() === '') {
        mensajesError.push('Ingresa un mensaje');
        errorMensaje.textContent = 'Ingresa un mensaje';
        hayErrores = true; // Se establece a true si hay un error
    } else {
        errorMensaje.textContent = '';
    }

    if (hayErrores) {
        return false; // Si hay errores, no se envía el formulario
    } else {
        return true; // Si no hay errores, se envía el formulario
    }
}


// Obtener el botón y el contenedor de video
var botonMostrarVideo = document.getElementById("mostrarVideo");
var videoContainer = document.getElementById("videoContainer");

// Añadir evento al botón para mostrar el video cuando se presiona
botonMostrarVideo.addEventListener("click", function() {
    // Mostrar el contenedor de video
    videoContainer.style.display = "block";
});


//reloj
function appendValue(value) {
    document.getElementById('input').value += value;
}

function clearInput() {
    document.getElementById('input').value = '';
}

function calculate() {
    var expression = document.getElementById('input').value;
    var result = eval(expression);
    document.getElementById('input').value = result;
}

function displayTime() {
    var now = new Date(); // Obtiene la fecha y hora actual
    var hours = now.getHours().toString().padStart(2, '0'); // Obtiene las horas y asegura que tenga dos dígitos (con ceros a la izquierda si es necesario)
    var minutes = now.getMinutes().toString().padStart(2, '0'); // Obtiene los minutos y asegura que tenga dos dígitos (con ceros a la izquierda si es necesario)
    var seconds = now.getSeconds().toString().padStart(2, '0'); // Obtiene los segundos y asegura que tenga dos dígitos (con ceros a la izquierda si es necesario)
    document.getElementById('clock').textContent = hours + ':' + minutes + ':' + seconds; // Actualiza el contenido del div con la hora actual en formato HH:MM:SS
}
setInterval(displayTime, 1000); // Llama a la función displayTime() cada segundo para actualizar el reloj
displayTime(); // Muestra la hora actual al cargar la página

//hasta aqui reloj


