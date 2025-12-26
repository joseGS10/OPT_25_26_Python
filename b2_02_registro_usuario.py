def registrar_usuario(nombre, edad, ciudad="Madrid"):
    """
       Esta función pone en practica las diferentes formas de llamarla
       según la forma en que le pasemos los argumentos: posicionales,
       nombrados, u omitiendo alguno de ellos porque se haya definido
       como parámetro con un valor por defecto
    """
    print(f"Usuario: {nombre}, Edad:{edad}, Ciudad:{ciudad}")

registrar_usuario("David", 14, "Huelva")
registrar_usuario("Maria", 42)
registrar_usuario(ciudad="Cadiz", nombre="Pepe", edad=33)
