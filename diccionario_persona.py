persona = {"nombre" : "Jose David", "edad" : 14, "ciudad" : "Huelva"}

for valor in persona.values():
    print(valor)

persona.update({"profesion" : "Estudiante"})

del persona["ciudad"]

print("Tras incluir profesión y eliminar ciudad, el dicionario contiene.....")
for clave, valor in persona.items():
    print(clave, ":", valor)




