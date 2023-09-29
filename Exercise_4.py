# Leer un numero enteros positivo desde teclado e imprimir la suma de los digitos que los componen

Ln_num = int(input("Ingresa un numero entero positivo: "))
Ln_add = 0

while Ln_num != 0:
    Ln_add += Ln_num % 10
    Ln_num = Ln_num // 10

print("La sumatoria de todos los numeros ingresados es: ", Ln_add)