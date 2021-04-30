# 49.	Escribe un algoritmo o el respectivo diagrama de flujo que lea n números y calcule su suma y su promedio

print("Vamos a calcular la suma y el promedio de cuantos numeros desee el usuario") # Informacion para el usuario

Suma = 0
Numeros = int(input("¿Cuantos número deseas ingresar? = "))

for i in range(1, Numeros + 1, 1):
    N = int(input("Ingresa un numero para sumar: "))
    Suma = Suma + N

Promedio = Suma / Numeros
print("La suma de los 10 numeros ingresados es --->", Suma)
print("El promedio de los 10 numeros ingresados es --->", Promedio)