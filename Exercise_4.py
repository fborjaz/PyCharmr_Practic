# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen

num_str = input("Ingresa un número entero positivo: ")

# Verificar si la entrada es un número entero positivo
if num_str.isdigit():
    num = int(num_str)
    digit_sum = sum(int(digit) for digit in num_str)
    print("La suma de los dígitos es:", digit_sum)
else:
    print("Por favor, ingresa un número entero positivo válido.")
