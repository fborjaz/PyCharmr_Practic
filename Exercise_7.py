# Programa que solicite al usuario una cantidad y luego itere la cantidad de cuces dada. En cada itereacion, solicitar al usuario que ingrese un numero. Al finalizar, mostrar la suma de tidis los numeros ingresados

try:
    Ln_repetition = int(input("Ingrese el numero de veces a repetir: "))

    if Ln_repetition <= 0:
        print("El numero de repeticiones debe ser mayor a 0")
    else:
        Ln_sum = 0

        for i in range(Ln_repetition):
            try:
                Ln_num = float(input(f"Ingrese el numero {i + 1}: "))
                Ln_sum += Ln_num
            except  ValueError:
                print("Error: Ingrese solo numeros")
    print(f"La suma de todos los numeros ingresado es: {Ln_sum}")

except ValueError:
    print("Error: Ingresar solo numeros")


