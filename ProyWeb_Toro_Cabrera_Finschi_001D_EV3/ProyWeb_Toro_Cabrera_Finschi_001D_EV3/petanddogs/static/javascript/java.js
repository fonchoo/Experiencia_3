
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

