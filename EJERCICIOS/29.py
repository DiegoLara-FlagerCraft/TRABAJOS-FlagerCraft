# Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine el mayor y el menor de ellos. 

print("Vamos a determinar entre tres numeros cual es el mayor y el menor")

Num1 = float(input("Ingresa un numero: "))
Num2 = float(input("Ingresa otro numero: "))
Num3 = float(input("Ingresa otro numero: "))
NumMay = 0
NumMen = 0

if Num1 > Num2:
    NumMay = Num1
    NumMen = Num2
else:
    NumMay = Num2
    NumMen = Num1

    if Num1 > Num3:
        NumMay = Num1
        NumMen = Num3
    else:
        NumMay = Num3
        NumMen = Num1

        if Num2 > Num3:
            NumMay = Num2
            NumMen = Num3
        else:
            NumMay = Num3
            NumMen = Num2

print("El numero Mayor es", NumMay, "y el numero menor es", NumMen)