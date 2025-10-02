usuario_correcto = "admin"
contraseña_correcta = "1234"
nombre = input("Nombre de usuario: ")
contraseña = input("Password: ")
if (nombre == usuario_correcto and contraseña == contraseña_correcta):
    print("Acceso concedido")
else:
    print("Acceso denegado")