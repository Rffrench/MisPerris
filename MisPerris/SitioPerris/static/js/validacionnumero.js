/*Funcion para validar que el campo telefono solo acepte numeros */
$('#telefono').on('input', function () {
    if (!/^[0-9]$/i.test(this.value)) {
        this.value = this.value.replace(/[^0-9]+/ig,"");
        alert("ERROR: Este campo solo acepta numeros")
    }
});
