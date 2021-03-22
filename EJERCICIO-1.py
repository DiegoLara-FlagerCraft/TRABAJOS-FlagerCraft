# Elabore un algoritmo que permita leer 10 números enteros positivos y los almacene 
# en un arreglo unidimensional, el algoritmo debe calcular la media de los 10 números ingresados.

Cont = 1
Num = 0
Sumatoria = 0
Media = 0
for num in range(1, 11, 1):
    Num = int(input("Ingrese un Numero Entero Positivo "))
    print("Numero [" + str(Cont) + "] = " + str(Num))
    Sumatoria += Num
    Cont += 1
Media = Sumatoria / 10
print("La Media de los Numeros es:", Media)