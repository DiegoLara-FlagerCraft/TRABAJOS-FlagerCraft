# Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es positivo o negativo. 

print("Vamos a determinar si un numero es negativo o positivo")

Num = float(input("Ingresa un numero: "))
if Num > 0:
    print("El numero ingresado es positivo")
elif Num < 0:
    print("El numero ingresado es negativo")
else:
    print("El numero ingresado es cero")