
$(document).ready(function(){
	$("#id_url").addClass("form-control")
				.attr("placeholder","ingrese aqui la URL")
				.attr("style","display:inline;width:68%; margin:8px 0px 0 0;")
				.val("http://");

	$("#id_username").addClass("form-control")
				.attr("placeholder","Nombre de usuario");

	$("#id_password").addClass("form-control")
				.attr("placeholder","Contraseña");

});
