# 48.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 números y calcule su suma y su promedio

print("Vamos a calcular la suma y el promedio de 10 numeros ingresados por el usuario") # Informacion para el usuario

Suma = 0

for i in range(1, 11, 1):
    N = int(input("Ingresa un numero para sumar: "))
    Suma = Suma + N

Promedio = Suma / 10
print("La suma de los 10 numeros ingresados es --->", Suma)
print("El promedio de los 10 numeros ingresados es --->", Promedio)