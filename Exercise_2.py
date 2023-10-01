# Ingrese un numero positivo y muestrelo, caso contrario solicite nuevamente el numero

while True:
    try:
        Ln_num = int(input('Ingrese un numero: '))
        if Ln_num > 0:
            print(f'El numero ingresado fue: {Ln_num}')
            break
        else:
            print('Error: Debe ingresar un numero positivo.')
    except ValueError:
        print('Error: Ingresar solo numeros')