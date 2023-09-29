Ln_num_str = ""
Ln_peers = 1

while Ln_num_str != "1":
    Ln_num_str = input("Ingrese un numero entero positivo: ")

    if Ln_num_str.isdigit():
        Ln_num = int(Ln_num_str)
        Ln_num_sum = sum(int(Ln_digit) for Ln_digit in Ln_num_str)
        print(f"La suma de los dígitos es: {Ln_num_sum}")

        if Ln_num % 2 == 0:
            Ln_peers += 1
    else:
        print("No ha ingresado un número entero positivo válido.")

print("La cantidad de números pares es:", Ln_peers)
