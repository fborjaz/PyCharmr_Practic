# Leer un numeor enteros de treclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los numeros ingresados

Ln_num = 1
Ln_add = 0

while Ln_num != 0:
    Ln_num = int(input("Ingresa otro numero: "))
    Ln_add += Ln_num

    if Ln_num == 0:
        break
    else:
        continue

print("¡Felicidades! Adivinaste el numero 0 correctamente")
print("La sumatoria de todos los numeros ingresados es: ", Ln_add)