def sumar(a,b):
    """ Función que devuelve la suma de dos valores pasados como argumentos"""
    return a+b

def restar(a,b):
    """ Función que devuelve la resta de dos valores pasados como argumentos"""
    return a-b

def multiplicar(a,b):
    """ Función que devuelva la multiplicación de dos valores pasados como argumentos"""
    return a*b

def dividir(a,b):
    """ Función que devuelve el resultado de la división de dos valores
        pasados como argumentos. Controla la división por 0 de forma que
        si se va a dividir por 0 no devuelve nada
    """
    if b!=0:
        return a/b

num1 = int(input("Intro un numero: "))
num2 = int(input("Intro otro numero: "))

print(f"La suma de {num1} y {num2} es {sumar(num1,num2)}")
print(f"La resta de {num1} y {num2} es {restar(num1,num2)}")
print(f"La multiplicación de {num1} y {num2} es {multiplicar(num1,num2)}")
resultado = dividir(num1, num2)
if resultado == None:
    print("No se pude dividir por 0. Operación indefinida")
else:
    print(f"La division de {num1} y {num2} es {dividir(num1,num2)}")




