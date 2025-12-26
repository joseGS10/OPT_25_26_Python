"""
    Este programa crea una lista vacia. A continuación, se le introducen
    5 productos solicitados por teclado y finañmente se realizan una serie de
    operaciones sobre la lista
"""
compras = [] # Definimos una lista vacía

print("Necesito que me proporciones 5 productos.")
for i in range(5):
    producto = input(f"Intro el producto {i+1}: ")
    compras.append(producto)

print(f"La lista queda asi: {compras}")

prod_eliminar = input("Dime que producto quieres eliminar: ")
compras.remove(prod_eliminar)

compras.sort()
print(f"La lista resultante ordenada alfabéticamente queda así: {compras}")



