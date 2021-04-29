# Escribe un algoritmo o el respectivo diagrama de flujo que lea dos números y determine el mayor de ellos. 

print("Vamos a determinar entre dos numeros cual es el mayor")

Num1 = float(input("Ingresa un numero: "))
Num2 = float(input("Ingresa otro numero: "))

if Num1 > Num2:
    print("El", Num1, "es el numero mayor")
if Num1 < Num2:
    print("El", Num2, "es el numero mayor")
if Num1 == Num2:
    print("Los numeros son iguales")