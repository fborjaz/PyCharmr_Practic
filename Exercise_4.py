# Leer un numero entero positivo desde teclado e imprimir la suma de la cantidad de digitos que tiene.

while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("El número ingresado no es positivo. Intente de nuevo.")
        else:
            cantidad_digitos = len(str(numero))
            print(f"La cantidad de dígitos en {numero} es {cantidad_digitos}")
            break
    except ValueError:
        print("Error: . Ingresar solo números.")
