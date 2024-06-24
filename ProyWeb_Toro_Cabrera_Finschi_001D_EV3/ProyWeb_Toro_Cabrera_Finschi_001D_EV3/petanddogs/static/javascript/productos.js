function clearErrors() {
            var errorElements = document.getElementsByClassName("error-message");
            while (errorElements[0]) {
                errorElements[0].parentNode.removeChild(errorElements[0]);
            }
        }
function validateForm() {
            clearErrors();
            var isValid = true;
            var id = document.forms["productForm"]["id"].value;
            var nombre = document.forms["productForm"]["nombre"].value;
            var descripcion = document.forms["productForm"]["descripcion"].value;
            var precio = document.forms["productForm"]["precio"].value;
            var stock = document.forms["productForm"]["stock"].value;
            var categoria = document.forms["productForm"]["categoria"].value;

            if (id == "") {
                showError("id", "El campo Id es obligatorio.");
                isValid = false;
            } else if (/\s/.test(id)) {
                showError("id", "El Id del producto no debe contener espacios en blanco.");
                isValid = false;
            }

            if (nombre == "") {
                showError("nombre", "El campo Nombre es obligatorio.");
                isValid = false;
            }

            if (descripcion == "") {
                showError("descripcion", "El campo Descripción es obligatorio.");
                isValid = false;
            }

            if (precio == "") {
                showError("precio", "El campo Precio es obligatorio.");
                isValid = false;
            } else if (isNaN(precio)) {
                showError("precio", "El Precio debe ser un número.");
                isValid = false;
            }

            if (stock == "") {
                showError("stock", "El campo Stock es obligatorio.");
                isValid = false;
            } else if (isNaN(stock)) {
                showError("stock", "El Stock debe ser un número.");
                isValid = false;
            }

            if (categoria == "") {
                showError("categoria", "El campo Categoría es obligatorio.");
                isValid = false;
            }

            return isValid;
        }

        function showError(fieldName, message) {
            var field = document.forms["productForm"][fieldName];
            var error = document.createElement("div");
            error.className = "error-message";
            error.innerHTML = message;
            field.parentNode.appendChild(error);
        }