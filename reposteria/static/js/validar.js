// Función para validar el Login
function validarLogin() {
    // Variables para el login
    var correo = "";
    var contraseña = "";
    var expresion = "";

    // Obtención de los elementos
    correo = document.getElementById("correo").value;
    contraseña = document.getElementById("contraseña").value;
    expresion = /^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;

    // Largo de las variables
    if (correo.length < 3 || correo.length > 30) {
        alert("Error, el correo debe tener un largo de mínimo 3 caracteres y máximo 10");
    }
    if (contraseña.length < 5 || contraseña.length > 15) {
        alert("Error, la contraseña debe tener un mínimo de 5 caracteres y máximo 15");
    }
    // Formato del correo
    if (!expresion.test(correo)){
        alert("Error, formato de correo invalido");
    }
    else {
        alert("Login exitoso!");
    }
}

// Función para validar el Registro
function validarRegistro() {
    // Variables para el registro
    var nombre = "";
    var apellido = "";
    var correo2 = "";
    var contraseña2 = "";
    var numero = "";
    var expresion = "";

    // Obtención de los elementos
    nombre = document.getElementById("nombre").value;
    apellido = document.getElementById("apellido").value;
    correo2 = document.getElementById("correo2").value;
    contraseña2 = document.getElementById("contraseña2").value;
    numero = document.getElementById("numero").value;
    expresion = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;

    // Largo de las variables
    if (nombre.length < 3 || nombre.length > 20) {
        alert("Error, el nombre debe tener un mínimo de 3 caracteres y máximo 20");
    }
    if (apellido.length < 3 || apellido.length > 20) {
        alert("Error, el apellido debe tener un mínimo de 3 caracteres y máximo 20");
    }
    if (correo2.length < 3 || correo2.length > 30) {
        alert("Error, el correo debe tener un largo de mínimo 3 caracteres y máximo 10");
    }
    if (contraseña2.length < 5 || contraseña2.length > 15) {
        alert("Error, la contraseña debe tener un mínimo de 5 caracteres y máximo 15");
    }
    // Verificar que el telefono sea un número
    if (isNaN(numero)){
        alert("El telefono ingresado no es un número")
    }
    // Formato del correo
    if (!expresion.test(correo)){
        alert("Error, formato de correo invalido");
    }
    else {
        alert("Registro exitoso!");
    }
}