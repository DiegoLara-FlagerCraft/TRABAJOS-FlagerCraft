agregar = "si"
def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while agregar == "si":
    numero = int(input("Ingrese el número a evaluar: "))
    if primo(numero):
        print("El número" + " " + str(numero) + " es primo." )
    else:
        print("El número" + " " + str(numero) + " no es primo." )
    agregar = input("¿Quieres agregar otro numero? si o no = ")
    if agregar == "no":
        print("No vuelva :D")