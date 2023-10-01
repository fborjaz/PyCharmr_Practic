# Crear un programa que le pida a un usuario una serie de numeros cualquiera y que solo dejaremos de hcaerlo cuando el usuario ingrese un numero igual a cero.

Ln_num = 1

while Ln_num != 0:
    try:
        Ln_num = int(input("Ingresa un numero: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")

print("¡Felicidades! Adivinaste el número 0 correctamente")

