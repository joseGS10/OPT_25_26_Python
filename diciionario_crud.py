#people = {"222222222": {"dni":"222222222", "nombre": "David", "age": 14, "city": "Huelva", "profesion": "Estudiente"},
#          "111111111": {"dni":"111111111", "nombre": "Ana", "age": 28, "city": "Cadiz", "profesion": "Azafata"}}

people = {}  # Main dictionary: {nif: {dni, name, age, city, profession}}


def create_person(person):
    """Create a new person and add to the dictionary."""
    # TODO: Ask for ID, name, age, city, profession and add to people

    if person["dni"] in people:
        print(f"La persona con dni {person["dni"]} ya existe. No se añadirá de nuevo")
    else:
        people[person["dni"]] = person
        print("Persona creada correctamente.")

def read_people():
    """Display all registered people."""
    # TODO: Loop through people and print their info
    for clave, valores in people.items():
        print(f"NIF: {clave} -> valores{valores}")

def update_person(dni_actualizar):
    """Update information of an existing person."""
    # TODO: Ask for ID, check if exists, and update fields
    # Si la persona a actualizar se encuentra registrada
    if dni_actualizar in people:
        print("Actualizaión de los valores de los campos. Intro si no se desea modificar.")
        for clave, valor in people[dni_actualizar].items():
            nuevo_valor = input(f"{clave} actual ({valor}): ")
            if nuevo_valor:
                # Convertir edad a entero si se edita
                if clave == "age":
                    people[nif_actualizar][clave] = int(nuevo_valor)
                else:
                    people[nif_actualizar][clave] = nuevo_valor
        print("Persona actualizada con éxito.")

    # Si la persona a actualizar no se encuentra registrada
    else:
        print(f"La persona de NIF {dni_actualizar} no existe aún")

def delete_person(dni_borrar):
    """Delete a person by ID."""
    # TODO: Ask for ID and remove from the dictionary if exists
    # Si la persona a eliminar está registrada
    if (dni_borrar) in people:
        del people[nif_borrar]
        print(f"La persona con NIF {dni_borrar} ha sido eliminada.")
    else:
        print(f"La persona con NIF {dni_borrar} no exite.")


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
            persona = {}
            nif = input("Introduzca su DNI: ")
            name = input("Introduzca su Nombre: ")
            age = int(input("Introduzca su edad: "))
            city = input("Introduzca su Ciudad: ")
            profession = input("Introduzca su profesion: ")
            persona = {"dni":nif, "name":name, "age":age, "city":city, "profession":profession}
            create_person(persona)

        case "2":
            read_people()

        case "3":
            nif_actualizar = input("Introduce nif de la persona a actualizar: ")
            update_person(nif_actualizar)

        case "4":
            nif_borrar = input("Intro nif de la persona a eliminar: ")
            delete_person(nif_borrar)

        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")