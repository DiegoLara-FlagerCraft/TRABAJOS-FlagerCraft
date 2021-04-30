# 51.	Construye un algoritmo y el respectivo diagrama de flujo que le solicite al usuario un 
# número entero positivo, si el usuario digita un valor no permito, le debe volver a pedir el número. 
# Una vez ingrese un valor válido deberá imprimir dicho valor.

print("Vamos a determinar si el numero que entra el usuario es entero positivo, si no le volvera a pedir el valor") # Informacion para el usuario

N = -1

while N < 0:
    N = int(input("Ingresa un numero entero positivo: "))
    if N > 0:
        print("El numero", N, "es entero positivo")
    elif N < 0:
        print("El numero ingresado no es entero positivo.... Vuelve a ingresarlo")