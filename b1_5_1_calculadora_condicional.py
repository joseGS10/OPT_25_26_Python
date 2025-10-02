num1 = int(input("Deme un número: "))
num2 = int(input("Deme otro número: "))
operacion = input("Elige operación (suma, resta, multiplicación, división): ")
if operacion == "suma":
    print(f"Resultado:  {num1} + {num2} =", num1 + num2)
elif operacion == "resta":
    print(f"Resultado: {num1} - {num2} =", num1 - num2)
elif operacion == ("multiplicacion"):
    print(f"Resultado: {num1} * {num2} =", num1 * num2)
elif operacion == "division":
    print(f"Resultado: {num1} / {num2} =", num1 / num2)
else :
    print("operación no valida")