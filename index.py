# import random
import random

def Advina_el_num(x):
    print("=============================================")
    print("| ¡Bienvenido al juego de advina el numero! |")
    print("=============================================")

    print("Tu meta es adivinar el numero generado por la computadora")

    Ln_num = random.randint(1, x) # numero aleatorio entre 1 y x.

    prediction = 0

    while prediction != Ln_num:
        prediction = int(input(f"Ingresa un numero entre 1 y {x}: "))
        if prediction < Ln_num:
            print("Lo siento, el numero es muy bajo. Intenta de nuevo")
        elif prediction > Ln_num:
            print("Lo siento, el numero es muy alto. Intenta de nuevo")

    print(f"¡Felicidades! Adivinaste el numero {Ln_num} correctamente")


Advina_el_num(10)