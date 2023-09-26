# Ingrese un numero positivo y muestrelo, caso contrario solicite nuevamente el numero

Ln_num = int(input("Ingrese un numero: "))

if Ln_num > 0:
    print(f"El numero ingresado fue: {Ln_num}")

while Ln_num < 0:
    Ln_num = int(input("Ingrese un numero positivo: "))
    if Ln_num > 0:
        print(f"El numero ingresado fue: {Ln_num}")
        break
    else:
        continue