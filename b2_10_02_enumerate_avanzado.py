estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

# Recorremos usando enumerate + zip
for indice, (est, mat, fis, qui) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):

    # Calcular promedio
    promedio = (mat + fis + qui) / 3

    # Determinar estado
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    # Mostrar reporte
    print(f"{indice} {est} - Matemáticas: {mat}, Física: {fis}, Química: {qui}, Promedio: {round(promedio,2)}, Estado: {estado}")




