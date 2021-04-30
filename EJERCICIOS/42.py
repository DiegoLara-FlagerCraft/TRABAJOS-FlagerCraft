# 42.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima los primeros 10 números naturales impares

print("Vamos a imprimir los primeros 10 números naturales impares") # Informacion para el usuario

for i in range(1, 20, 1):
    if i % 2 != 0:
        print(i)