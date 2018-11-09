/*Funcion para validar que el campo de nombre de usuario solo acepte los caracteres siguientes :a-z A-Z áéíóúüñ*/
$('#nombre').on('input', function () {
    if (!/^[ a-z A-Z áéíóúüñ]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^ a-z A-Z áéíóúüñ]+/ig,"");
        alert("ERROR: Este campo solo acepta letras");
    }
});
