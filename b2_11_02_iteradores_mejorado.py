estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

#it es un iterador del diccionario estudiantes
it =iter(estudiantes)

while True:
    # Usamos next con valor por defecto None como centinela
    elemento = next(it, None)

    # Si el iterador terminó, salimos del while
    if elemento is None:
        break

    nombre = elemento
    notas = estudiantes[nombre]

    # Calcular promedio
    promedio = sum(notas) / len(notas)

    # Determinar estado
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    #Imprimir resultados
    print(f"{nombre} - Notas: {notas}, Promedio: {round(promedio,2)}, Estado: {estado}")