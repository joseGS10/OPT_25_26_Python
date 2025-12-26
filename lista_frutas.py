frutas = ["manzana", "platano", "fresa", "kiwi", "uva"]
print(f"La lista inicialmente contiene {frutas}")

print(f"La primera fruta de la lista es {frutas[0]}")
print(f"La última fruta de la lista es {frutas[-1]}")

#Vamos a cambiar de posicion la manzana con la fresa
print("Vamos a cambiar de posición la manzana con la fresa.")
indice1 = frutas.index("manzana")
indice2 = frutas.index("fresa")
aux = frutas[indice1]
frutas[indice1] = frutas[indice2]
frutas[indice2] = aux
print(f"La lista tras el cambio queda asi: {frutas}")

#añadimos una fruta a la lista
print("Añadimos la fruta Kaki al final de la lista")
frutas.append("Kaki")
print(f"La lista contiene ahora: {frutas}")

#eliminamos una fruta de la lista
print("Vamos a eliminar la fruta 'uva' de la lista")
frutas.remove("uva")
print(f"La lista FINAL contiene: {frutas}")




