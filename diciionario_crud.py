#people = {"123456789": {"nombre": "David", "age": 14, "city": "Huelva", "profesion": "Estudiente"},
#          "987654321": {"nombre": "Ana", "age": 28, "city": "Cadiz", "profesion": "Azafata"}}

people = {}  # Main dictionary: {nif: {name, age, city, profession}}


def create_person(person):
    """Create a new person and add to the dictionary."""
    # TODO: Ask for ID, name, age, city, profession and add to people
    key = person.get("dni")
    people[key] = person


def read_people():
    """Display all registered people."""
    # TODO: Loop through people and print their info
    print(people)
    """
        for clave, valores in people.items():
        print(f"NIF: {clave} -> valores{valores}")
    """

def update_person():
    """Update information of an existing person."""
    # TODO: Ask for ID, check if exists, and update fields
    person = {"dni": "442077778F", "nombre":"Pepe", "age": 19, "ciudad":"Huelva"}
    key = person.get("dni")
    if key in people:
        people[key] = person
    else:
        print("No existe ese usuario")
    """
    nif_actualizar = input("Introduce nif de la persona a actualizar: ")
    if nif_actualizar in people:
        print("Actualizaión de los valores de los campos. Intro si no se desea modificar.")
        for campo, valor in people[nif_actualizar].items():
            nuevo_valor = input(f"{campo.capitalize()} actual ({valor}): ")
            if nuevo_valor:
                # Convertir edad a entero si se edita
                if campo == "age":
                    people[nif_actualizar][campo] = int(nuevo_valor)
                else:
                    people[nif_actualizar][campo] = nuevo_valor

        print("Persona actualizada con éxito.")
    #if nif_actualizar not in people:
    else:
        print(f"La persona de NIF {nif_actualizar} no existe aún")
    """
def delete_person():
    """Delete a person by ID."""
    # TODO: Ask for ID and remove from the dictionary if exists
    del people["44207778F"]
    """
    nif_borrar = input("Intro nif de la persona a eliminar: ")
    if (nif_borrar) in people:
        del people[nif_borrar]
        print(f"La persona con NIF {nif_borrar} ha sido eliminada.")
    else:
        print(f"La persona con NIF {nif_borrar} no exite.")
    """

# 🔸 Main menu
option = ""

while option != "5":
    print("\n=== PEOPLE CRUD MENU ===")
    print("1. Create person")
    print("2. Read people")
    print("3. Update person")
    print("4. Delete person")
    print("5. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
            persona={}
            nif = input("Introduzca su DNI: ")
            name = input("Introduzca su Nombre: ")
            age = int(input("Introduzca su edad: "))
            city = input("Introduzca su Ciudad: ")
            profession = input("Introduzca su profesion: ")

            persona= {"name" : name, "age" : age, "city" : city, "profession" : profession}

            create_person(persona)
            print("Persona creada correctamente.")
        case "2":
            read_people()
        case "3":
            update_person()
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")