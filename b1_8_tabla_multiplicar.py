"""
    Este programa te solicita un número y
    te muestra la tabla de multiplicar del 1-10
"""
num_tabla = int(input("Dame un número: "))

# bucle que se ejecuta 10 veces desde numero = 1 hasta numero = 10
for numero in range(1,11):
    print(f"{num_tabla} x {numero} =", num_tabla * numero)




