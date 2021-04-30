# 52.	Construye un algoritmo y el respectivo diagrama de flujo que permita leer una 
# cantidad variable de números y nos indique cuantos fueron mayores a 100 y cuántos menores a 100.

print("Vamos a determinar si los valores que ingrese el usuario son mayores o menores que 100") # Informacion para el usuario

ContMay = 0
ContMen = 0
ContIgu = 0
N = int(input("¿Cuantos numeros deseas ingresar? = "))

for i in range(1, N + 1, 1):
    N = float(input("Ingresa un numero: "))
    if N > 100:
        ContMay = ContMay + 1
    if N < 100:
        ContMen = ContMen + 1
    if N == 100:
        ContIgu = ContIgu + 1

print(ContMay, "numeros fueron Mayores a 100")
print(ContMen, "numeros fueron Menores a 100")
print(ContIgu, "numeros fueron Iguales a 100")