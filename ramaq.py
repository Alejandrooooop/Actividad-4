# Calculadora simple en Python


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0.")
    return a / b


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion not in {"1", "2", "3", "4"}:
        print("Opción inválida. Intenta de nuevo.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar números válidos.")
        continue

    try:
        if opcion == "1":
            resultado = sumar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "2":
            resultado = restar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "4":
            resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")
    except ValueError as e:
        print(e)
