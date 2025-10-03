"""
Al realizar la operación promedio hay que tener en cuenta
la precedencia de las operaciones y en este caso tal y como
está expresada la operación promedio, sabemos que la operación
se lleva a cabo de izq a dcha. Por lo que suma nota1 con nota2,
y a continuación como la división tiene preferencia sobre la suma,
primero divide nota3 entre 3 y finalmente suma este resultado al
resultdo obtenido de sumar nota1 + nota2
"""
nota1 = float(input("Dame la primera nota: "))
nota2 = float(input("Dame la segunda nota: "))
nota3 = float(input("Dame la tercera nota: "))

# la siguiente linea presenta un error lógico
# print("La media de las tres notas es: ", nota1 + nota2 + nota3 / 3)

# A continuación aparece la linea corregida
print("La media de las tres notas es: ", (nota1 + nota2 + nota3) / 3)