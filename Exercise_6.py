Ln_Opction = 0

while Ln_Opction != 3:
    print('Menu')
    print('1.- Comenzar el Programa')
    print('2.- Imprimir el listado')
    print('3.- Finalizar')

    Ln_select_op = int(input("Escoja  una opcion del menu: "))

    if  Ln_select_op == 1:
        print('El programa a iniciado')
    elif Ln_select_op == 2:
        print('Hola soy una lista')
    elif Ln_select_op == 3:
        print('Gracias por usar el sistema')
        Ln_Opction = 3