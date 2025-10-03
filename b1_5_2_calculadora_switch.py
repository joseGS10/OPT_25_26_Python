num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
operacion = input("Indicame una operacion (+, -, *, /):")

match operacion:
    case '+':
        print(f"La suma de {num1} + {num2} es ", num1 + num2)
    case '-':
        print(f"La resta de {num1} - {num2} es " ,num1 - num2)
    case '*':
        print(f"La multiplicación de {num1} * {num2} es ", num1 * num2)
    case '/':
        print(f"La división de {num1} / {num2} es ", num1 /num2)
    case _:
        print("operación no reconocida")

