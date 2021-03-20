# Pedir al usuario que ingrese un número entero positivo e imprimir todos los números
# correlativos entre el ingresado por el usuario y uno menos del doble del mismo.

n = int(input("Ingrese un Numero entero Positivo: "))
Doble = n * 2
for n in range(n, Doble, 1):
    print(n)
