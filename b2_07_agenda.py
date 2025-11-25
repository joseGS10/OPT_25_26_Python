"""
    Este programa solicita por teclado tres pares de clave,valor y las
    guarda en el doccionario agenda. Posteriormente imprime el contenido
    del diccionario y por ultimo solicita un contacto el cual busca en
    el diccionario y devuelva su telefono si existe el contacto o mensaje
    de no encontrado en caso contrario
"""

agenda = {}
print("Introduce 3 contactos.")

for i in range(3):
    nombre = input (f"Intro nombre contacto_{i+1}: ")
    telefono = input (f"Intro tlfno contacto_{i+1}: ")
    agenda.update({nombre:telefono})

print()
print("Agenda completa")
print("---------------")
for clave,valor in agenda.items():
    print(clave, ":", valor)

print()
contacto = input ("Buscar contacto: ")

if contacto in agenda:
    print(f"Teléfono: {agenda[contacto]}")
else:
    print("Contacto no encontrado")

