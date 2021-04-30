# 44.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima los n primeros números naturales

print("Vamos a imprimir los numeros naturales desde el 1 hasta el numero que el usuario elija") # Informacion para el usuario

N = int(input("¿Hasta que número deseas imprimir los numeros naturales? = "))

for i in range(1 , N + 1, 1):
    print(i)