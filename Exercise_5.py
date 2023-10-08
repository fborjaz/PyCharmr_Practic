# Solicitar al usuario que ingrese numeros enteros positivos y, por cada uno, imprimir la suma de los digitos que lo componen. La condicion de corte es que se ingrese el numero -1. Al finalizar, mostrar cuantos de los numeros ingresados por el usuario fieron numeros pares

Ln_num = 0
Ln_sum = 1
Ln_par = 0

while Ln_num != -1:
    try:
        Ln_num = int(input("Ingrese un número entero positivo: "))
        if Ln_num < -1:
            print('El número ingresado no es positivo. Intente de nuevo.')
        else:
            digitos = str(Ln_num)
            for digito in range(len(digitos)):
                Ln_sum += + digito

        if Ln_num % 2 == 0:
            Ln_par += + 1

    except:
        print('Error: Ingresar solo numeros')

print(f"La cantidad de pares ingresados son: {Ln_par}")
print(f"La cantidad total de digitos ingresados es: {Ln_sum}")