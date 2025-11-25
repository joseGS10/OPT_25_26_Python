"""
    Este programa intenta poner en practica el uso de comprensiones de listas
    y diccionarios
"""

lista = []

# generamos una lista de 20 números enteros
for numeros in range(1,21):
    lista.append(numeros)

# mediante comprensión de listas:

# Obtenemos una lista con los cuadrados de todos los numeros de la lista
cuadrados =[n ** 2 for n in lista]

# Obtenemos una lista con solo los pares
pares = [n for n in lista if n % 2 ==0]

# Obtenemos lista con números mayores a 10
mayores = [n for n in lista if n > 10]

# Creación de un diccionario con cada valor de la lista y su doble
dobles = {n: 2*n  for n in lista}

#Imprimimos el contenido de las diferentes listas y el diccionario
print(f"Lista original: {lista}")
print(f"Lista de cuadrados:  {cuadrados}")
print(f"Lista de pares: {pares}")
print(f"Lista de mayores de 10: {mayores}")
print(f"Dicccionario: {dobles}")