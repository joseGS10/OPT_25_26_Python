contador = 0

def incrementar():
    """ Función que incrementa en 1 el valor de la variable global contador"""
    global contador
    contador += 1

def decrementar():
    """ Función que decrementa en 1 el valor de la variable global contador"""
    global contador
    contador -= 1

def mostrar_contador():
    """ Función que muestra el valor de la variable global contador"""
    print(f"El valor de la variable global contador es {contador}")

incrementar()
incrementar()
decrementar()
mostrar_contador()


