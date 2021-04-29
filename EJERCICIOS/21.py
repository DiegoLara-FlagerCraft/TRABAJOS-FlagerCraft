# Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es par o impar. 

print("Vamos a determinar si un numero es par o impar")

Num = int(input("Ingresa un numero entero: "))
if Num % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")