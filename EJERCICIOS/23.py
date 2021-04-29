# Escribe un algoritmo o el respectivo diagrama de flujo que lea un número e indique 
# si este es par-positivo, par-negativo, impar-positivo o impar-negativo

print("Vamos a determinar si un numero es par-positivo, par-negativo, impar-positivo o impar-negativo")

Num = float(input("Ingresa un numero: "))
if Num % 2 == 0 and Num > 0:
    print("El numero ingresado es par-positivo")
elif Num % 2 == 0 and Num < 0:
    print("El numero ingresado es par-negativo")

if Num % 2 != 0 and Num > 0:
    print("El numero ingresado es impar-positivo")
elif Num % 2 != 0 and Num < 0:
    print("El numero ingresado es impar-negativo")
