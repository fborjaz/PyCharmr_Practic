# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen

Ln_num_str = input("Ingresa un número entero positivo: ")

# Verificar si la entrada es un número entero positivo
if Ln_num_str.isdigit():
    num = int(Ln_num_str)
    Ln_digit_sum = sum(int(Ln_digit) for Ln_digit in Ln_num_str)
    print("La suma de los dígitos es:", Ln_digit_sum)
else:
    print("Por favor, ingresa un número entero positivo válido.")
