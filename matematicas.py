def area_rentangulo(base, altura):
    """ Función que devuelve el area de un rectangulo """
    return base*altura

def perimetro_reectangulo(base, altura):
    """Función que devuelve el perímetro de un rentangulo"""
    return (base+altura)*2

base = int(input("Introduce la base: "))
altura = int(input("Introduce la altura: "))

print(f"El area del rectangulo es {area_rentangulo(base,altura)}")
print(f"El perímetro del rectangulo es {perimetro_reectangulo(base,altura)}")



