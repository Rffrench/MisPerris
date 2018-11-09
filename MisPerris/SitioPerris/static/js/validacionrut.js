/*funcion que valida que en el campo rut solo se ingresen los caracteres numericos del 0-9 luego el guion y finalmente del 0-9 y k K */
$('#run').on('focusout', function () {
    if (/^([0-9]+-[0-9Kk])$/i.test(this.value)){
     alert("El run " + this.value + " es correcto.");
 }else {
   alert("El run" + this.value + "es incorrecto.");
  }
});
