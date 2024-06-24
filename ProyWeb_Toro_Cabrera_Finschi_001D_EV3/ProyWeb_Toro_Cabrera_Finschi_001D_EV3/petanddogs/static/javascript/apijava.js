function getAdopcion(done) {
    const results = fetch("https://huachitos.cl/api/animales/comuna/127");

    results
        .then(response => response.json())
        .then(data => {
            done(data.data); // Enviamos solo el array de datos al callback
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
}

getAdopcion(data => {
    data.forEach(animal => {
        const article = document.createRange().createContextualFragment(/*html */`
            <article>
                <div class="image-container">
                    <img src="${animal.imagen}" alt="${animal.nombre} style="max-width: 100px; height: auto;">
                </div>
                <h2>${animal.nombre}</h2>
                <span>${animal.tipo}</span>
                <p>${animal.desc_fisica}</p>
                <p>${animal.desc_personalidad}</p>
            </article>
        `);
        const main = document.querySelector("main");
        main.append(article);
    });
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