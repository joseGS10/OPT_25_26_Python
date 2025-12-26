# Uso de la función zip() von 3 listas imprimiendo los pares coincidentes

nombre = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

for nomb, mat, fis in zip(nombre, notas_matematicas, notas_fisica):
    print(f"{nomb} - Matemáticas: {mat}, Física: {fis}")

