estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

resultado_final = {}

# recorremos todas las lista a la vez con zip() y sacamos el promedio de cada
# estudiante, su estado y almacenamos en un dicionario toda la informacion
# en cada iteracion del bucle
for est, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

    #calculo del promedio
    promedio = (mat + fis + qui)/3

    #calculo del estado
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    resultado_final[est] = {"Matematicas": mat,
                            "Fisica": fis,
                            "Quimica": qui,
                            "Promedio": round(promedio, 2),
                            "Estado": estado}

# Imprimimos el diciionario de datos resultante
for est, datos in resultado_final.items():
    # accedemos al diccionario para sacar el valor de cada estudiante
    print(f"{est} - Matemáticas: {datos["Matematicas"]}, Física: {datos["Fisica"]}, Química: {datos["Quimica"]}, Promedio: {datos["Promedio"]}, Estado: {datos["Estado"]}")





