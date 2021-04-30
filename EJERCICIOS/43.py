# 43.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima los primeros 10 números naturales pares

print("Vamoas a imprimir los primeros 10 numeros naturales pares") # Informacion para el usuario

for i in range(1, 21, 1):
    if i % 2 == 0:
        print(i)