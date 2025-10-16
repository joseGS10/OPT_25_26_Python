'''
Este programa consiste en un sistema que simula el registro e inicio de sesión
con validación de contraseñas seguras al igual que trabajan apps reales
'''

opcion = "0"
emails = [] # se inicializa la lista de emails validos a vacio
passwords = [] # se inicializa la lista de pqsswords validos a vaci0
# con este while se asegura que mientras la opcion seleccionada no sea la 3 se mostrará el menú de opciones
while opcion != 3:

    opcion = int(input("[1]. Registrarse [2]. Iniciar sesión [3]. Salir. Seleccione una tarea: "))

    match opcion:
        case 1:
            # Registro de usuarios
            caracteres_esp = "!@-$%&*?"
            contrasenavalida = False
            num_intentos_password = 3
            num_intentos_email = 3

            print("Opción Registro.")
            print("----------------")

            # solicitud del email de usuario y verificación reglas aceptación
            while (num_intentos_email > 0): # maximo número intentos intro email
                identifer = input("Introduzca su email: ")
                n_caracteres_email = 0
                cuenta_arrobas = 0
                cuenta_puntos = 0
                pos_punto = 0
                pos_arroba = 0
                emailvalido = True
                # se recorre el email comprobando los diferentes caracteres que lo forman para una primera criba
                for caracter in identifer:
                    n_caracteres_email += 1
                    # se cuentas arrobas existentes y se en caso de haber mas de una se guarda la posicion de la ultima
                    # encontrada
                    if caracter == "@":
                        cuenta_arrobas += 1
                        pos_arroba = n_caracteres_email - 1
                    if caracter == ".":
                        cuenta_puntos += 1
                        pos_punto = n_caracteres_email -1
                    # se comprueban los caracteres permitidos
                    if not(('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z') or ('0' <= caracter <= '9') or
                    (caracter == ".") or (caracter == '@')):
                        emailvalido = False
                        print ("El email contiene caracteres no permitidos")

                # Una vez recorrido y sabiendo que esta formado solo por caracteres permitidos, se comprueba si se
                # cumplen o no todos los requisitos para terminar de validar el email
                if emailvalido:
                    if n_caracteres_email < 6: # 6 es el minimo exigido; p.ej: a@b.es
                        emailvalido = False
                        print("El número de caracteres del email es inferior al exigido")
                    elif cuenta_arrobas != 1:
                        emailvalido = False
                        print("EL email tiene un numero inadecuado de @")
                    elif cuenta_puntos != 1:
                        emailvalido = False
                        print("El email tiene un número inaecuado de .")
                    # si llegamos hasta aqui es porque el email se compone solo de caracteres permitidos pero
                    # hay que ver si el @ y el . estan bien colocados
                    elif pos_arroba > pos_punto:
                        emailvalido = False
                        print("El @ y el . no estan donde les corresponde")
                    elif pos_arroba < 1:
                        emailvalido = False
                        print("El @ no puede ser el primer caracter del email")
                    elif pos_punto == pos_arroba + 1:
                        emailvalido = False
                        print("El @ y el punto no pueden ir seguidos.Debe haber un nombre de dominio entre medios")

                # Sabiendo que hasta el punto el email va correcto, queda por comprobar la extension .es, .com, .net
                if emailvalido:
                    extension = n_caracteres_email - (pos_punto + 1)
                    if (extension == 2 and identifer[pos_punto+1] == 'e' and identifer[pos_punto+2] == 's' and
                    n_caracteres_email == pos_punto +3) or (extension == 3 and identifer[pos_punto+1] == 'c' and
                    identifer[pos_punto+2] == 'o' and identifer[pos_punto+3] == 'm' and
                    n_caracteres_email == pos_punto +4) or (extension == 3 and identifer[pos_punto+1] == 'n' and
                    identifer[pos_punto+2] == 'e' and identifer[pos_punto+3] == 't' and n_caracteres_email == pos_punto +4):
                        emailvalido = True
                        #El email cumple todos los requisitos
                        break
                    else:
                        emailvalido = False
                        print("El email no es correcto. Fallo en la extensión")
                num_intentos_email -= 1
                if not emailvalido:
                    print (f"Número de intentos restantes {num_intentos_email}")
            if num_intentos_email == 0:
                print ("Usuario no registrado. Se apagará el sistema....bye")
                break


            #solicitud de la password y verificación reglas aceptación
            while (num_intentos_password > 0): #máximo número intentos para password
                password = input("Introduzca su password: ")
                n_caracteres = 0 # contador de caracteres de la contraseña
                mayuscula = False
                minuscula = False
                car_esp = False

                # se recorre la contraseña comprobando los diferentes requisitos exigidos
                for caracter in password:
                    n_caracteres += 1 #contabiliza cada caracter de la contraseña
                    #se comprueba si tiene alguna mayúscula
                    if (not mayuscula): # con este if se consigue que una vez encuentre una mayúscula no siga buscando mayúsculas con los siguientes caracteres
                        if caracter >= 'A' and caracter <= 'Z':
                            #La contraseña contiene al menos una mayúscula
                            mayuscula = True

                    #se compruba si tiene alguna minúscula
                    if (not minuscula):
                        if caracter >= 'a' and caracter <= 'z':
                            #La contraseña contiene al menos una minúscula
                            minuscula = True

                    #se compruba si tiene algún caracter especial
                    if caracter in caracteres_esp:
                        #La contraseña contiene al menos un caracter especial
                        car_esp = True


                # validar contraseña
                if (mayuscula == True) and (minuscula == True) and (car_esp == True) and n_caracteres >= 8:
                    #contraseña validada
                    contrasenavalida = True
                    break
                else:
                    print("Contraseña incorrecta")
                    if (mayuscula == False):
                        print ("La contraseña no contiene ninguna mayúscula")
                    if (minuscula == False):
                        print ("La contraseña no contiene ninguna minúscula")
                    if (car_esp == False):
                        print ("La contraseña no contiene ningún caracter especial")
                    if  (n_caracteres < 8):
                        print ("El número de caracteres de la contraseña es inferior a 8.")

                    num_intentos_password -= 1
                    print (f"Vuelva a intentarlo. Número de intentos restantes {num_intentos_password}")
            if num_intentos_password == 0:
                print ("Usuario no registrado. Se apagará el sistema....bye")
                break

            # si el email introducido y la password son valido los almacenamos en 2 listas

            if emailvalido and contrasenavalida:
                emails = emails + [identifer]
                passwords = passwords + [password]
                print(f"Usuario: {identifer} y contraseña: {password} almacenados correctamente.")


        case 2:
            # Inicio de sesión
            usuario_correcto = False
            print("Inicio de sesión")
            usuario = input("Introduce usuario: ")
            contador = 0
            for _ in emails:    # contamos los emails(usuarios que hay)
                contador += 1
            i = 0
            while i < contador and not usuario_correcto:
                if usuario == emails[i]:
                    usuario_correcto =  True
                else:
                    i += 1
            if usuario_correcto:
                clave = input("Intro su contraseña: ")
                n_intentos = 1
                while  clave != passwords[i] and n_intentos < 3:
                    print(f"Contraseña incorrecta. Intento {n_intentos}/3 fallido")
                    n_intentos += 1
                    clave = input("Intro su contraseña: ")

                if clave == passwords[i]:
                    print(f"Acceso concedido. Bienvenid@ {usuario}")
                else:
                    print("Demasiados intentos fallidos. Regresando al menú principal...")
            else:
                print(f"El usuario {usuario} no existe")

        case 3:
            #Abandonar el programa
            print("Saliendo del programa.....")

        case _:
            #Manejo opcion incorrecta
            print("Elección incorrecta.")

    print ("\n" * 3)