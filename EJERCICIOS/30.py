# Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y 
# determine si la suma del primero y el segundo es mayor o menor que el tercero. 

print("Vamos a determinar a partir de tres numero si la suma del primero y el segundo es mayor o menor al tercero")

Num1 = float(input("Ingresa un numero: "))
Num2 = float(input("Ingresa otro numero: "))
Num3 = float(input("Ingresa otro numero: "))
Suma = Num1 + Num2

if Suma > Num3:
    print("La suma de los dos primeros numeros es Mayor al tercer numero")
if Suma < Num3:
    print("La suma de los dos primeros numeros es Menor al tercer numero")
if Suma == Num3:
    print("La suma de los dos primeros numeros es Igual al tercer numero")