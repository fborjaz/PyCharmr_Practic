# Crear un programa que le pida a un usuario una serie de numeros cualquiera y que solo dejaremos de hcaerlo cuando el usuario ingrese un numero igual a cero.

Ln_num = int(input("Ingresa un numero: "))
while Ln_num != 0:
    Ln_num = int(input("Ingresa otro numero: "))
    if Ln_num == 0:
        break
    else:
        continue

print("¡Felicidades! Adivinaste el numero 0 correctamente")
