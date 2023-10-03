# # # Ejercicio 1 de la semana 3
# # # Crear un programa que le pida a un usuario una serie de numeros cualquiera y solo dejaremos de hacerlo cuando el usuario ingrese el numero 0
#
# Ln_num = 1
#
# while Ln_num != 0:
#     try:
#         Ln_num = int(input("Ingrese un numero: "))
#         print(f"El numero ingresado es: {Ln_num}")
#
#         if Ln_num == 0:
#             print("El numero ingresado es 0, el programa ha finalizado")
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número válido.")
#
#
# # Ejercicio 2 de la semana 3
# # Ingrese un numero positivo y muestrelo caso contrario solicite nuevamente el numero
#
# Ln_numbers = 0
#
# while Ln_numbers <= 0:
#     try:
#         Ln_numbers = int(input("Ingrese un numero positivo: "))
#         if Ln_numbers <= 0:
#             print("El numero ingresado es negativo o cero, por favor ingrese un numero positivo")
#         else:
#             print(f"El numero ingresado es: {Ln_numbers}")
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número válido.")
#
#
# # Ejercicio 3 de la semana 3
# # Leer numeros enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los numeros ingresados.
#
# Ln_numbers = 1
# Ln_sum = 0
#
# while Ln_numbers != 0:
#     try:
#         Ln_numbers = int(input("Ingrese un numero: "))
#         Ln_sum += Ln_numbers
#         print(f"El numero ingresado es: {Ln_numbers}")
#         print(f"La sumatoria de los numeros ingresados es: {Ln_sum}")
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número válido.")

# Ejercicio 4 de la semana 3
# Leer un numero entero positivo desde teclado e imprimir la suma de la cantidad de digitos que lo componen.

Ln_numbers = 0

# while Ln_numbers <= 0:
#     try:
#         Ln_numbers = int(input("Ingrese un numero positivo: "))
#         if Ln_numbers <= 0:
#             print("El numero ingresado es negativo o cero, por favor ingrese un numero positivo")
#         else:
#             print(f"El numero ingresado es: {Ln_numbers}")
#             num_str = str(Ln_numbers)
#             digit_count = len(num_str)
#             print(f"La cantidad de digitos en el numero ingresado es: {digit_count}")
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número válido.")

# Ejercicio 5 de la semana 3
# Solitar al usuario que ingrese un numero entero positivo y, por cada uno, imprimir la suma de los digitos que lo componen. La condicion de corte es que se ingrese el numero -1. Al finalizar, mostrar cuantos numeros ingresados por el usario fueron pares

Ln_numbers = 0
Ln_even_count = 0
Ln_digit_sum = 0

while Ln_numbers != -1:
    try:
        Ln_numbers = int(input("Ingrese un número: "))
        if Ln_numbers == -1:
            print("El número ingresado es -1. El programa ha finalizado.")
        elif Ln_numbers < 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            print(f"El número ingresado es: {Ln_numbers}")

            num_str = str(Ln_numbers)
            digit_count = len(num_str)
            print(f"La cantidad de dígitos en el número ingresado es: {digit_count}")

            Ln_digit_sum += Ln_digit_sum

            if Ln_numbers % 2 == 0:
                Ln_even_count += 1

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")

print(f"Total de números pares ingresados: {Ln_even_count}")
print(f"Suma de la cantidad de dígitos: {Ln_digit_sum}")



