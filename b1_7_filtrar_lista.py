"""
Este programa recorre una Lista e
imprime todos los elementos de ella
que no comienzan por la letra a/A
"""
nombres = ["Jose", "David", "Maria", "Juan", "Ana", "Andres"]

for nombre in nombres:
    if nombre[0] == 'A' or nombre[0] == 'a': # se compara el primer carácter de cada nombre
                                             # con la letra "a" minúscula o "A" mayúscula
        continue
    print(nombre)



