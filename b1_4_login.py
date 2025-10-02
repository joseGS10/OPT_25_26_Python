usuario_correcto = "admin"
contrasena_correcta = "1234"
nombre = input("Nombre de usuario: ")
contrasena = input("Password: ")
if (nombre == usuario_correcto and contrasena == contrasena_correcta):
    print("Acceso concedido")
else:
    print("Acceso denegado")