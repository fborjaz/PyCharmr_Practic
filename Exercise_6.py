# Reakuzar un menu con 3 opciones y al seleccionar donde si escoje una una opcion incorrecta informe el error y si escoje la opciones (1 o 2) muestre un mensaje y si eleije la 3 se interrumpira el menu y el progrmana finaliza

while True:
    print('Menu')
    print('1.- Comenzar el Programa')
    print('2.- Imprimir el listado')
    print('3.- Finalizar')

    try:
        Ln_select_op = int(input("Escoja  una opcion del menu: "))

        if  Ln_select_op == 1:
            print('El programa a iniciado')
        elif Ln_select_op == 2:
            print('Hola soy una lista')
        elif Ln_select_op == 3:
            print('Gracias por usar el sistema')
            break
        else:
            print('La opcion ingresada no existe')

    except ValueError:
        print('Error: Ingrese solo numeros')