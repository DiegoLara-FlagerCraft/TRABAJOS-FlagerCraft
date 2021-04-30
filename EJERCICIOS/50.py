# 50.	Escribe un algoritmo o el respectivo diagrama de flujo para leer una cantidad variable de 
# números e indicar el promedio de los números pares y el promedio de los números impares.

print("Vamos a calcular el promedio de cuantos numeros desee el usuario, tanto el promedio de los numeros pares como impares") # Informacion para el usuario

SumaPar = 0
SumaImpar = 0
ContadorPar = 0
ContadorImpar = 0
Numeros = int(input("¿Cuantos número deseas ingresar? = "))

for i in range(1, Numeros + 1, 1):
    N = int(input("Ingresa un numero para sumar: "))
    if N % 2 == 0:
        SumaPar = SumaPar + N
        ContadorPar = ContadorPar + 1
    if N % 2 != 0:
        SumaImpar = SumaImpar + N
        ContadorImpar = ContadorImpar + 1

if ContadorPar > 0: 
    PromedioPar = SumaPar / ContadorPar
    print("El promedio de los numeros pares es:", PromedioPar)
elif ContadorPar == 0:
    print("No se ingresaron numeros Pares")
if ContadorImpar > 0:
    PromedioImpar = SumaImpar / ContadorImpar
    print("El promedio de los numeros impares es:", PromedioImpar)
elif ContadorImpar == 0:
    print("No se ingresaron numeros Impares")