# Leer un numero entero positivo desde teclado e imprimir la suma de la cantidad de digitos que tiene.

while True:
    try:
        Ln_num = int(input("Ingrese un número entero positivo: "))
        if Ln_num < 0:
            print("El número ingresado no es positivo. Intente de nuevo.")
        else:
            cantidad_digitos = len(str(Ln_num))
            print(f"La cantidad de dígitos en {Ln_num} es {cantidad_digitos}")
            break
    except ValueError:
        print("Error: . Ingresar solo números.")
