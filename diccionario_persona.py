persona = {"nombre" : "David", "edad" : 14, "ciudad" : "Huelva"}

for valor in persona.values():
    print(valor)

persona["profesion"] = "pintor"

del persona["ciudad"]

for clave,valor in persona.items():
    print(clave, ":" , valor)





