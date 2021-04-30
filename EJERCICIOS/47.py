# 47.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la suma de los números naturales 
# contenidos entre dos números n y m (verificar que m>n)

print("Vamos a calcular la suma de los numeros naturales contenidos entre dos numeros elejidos por el usuario") # Informacion para el usuario

N = 1
M = 0
Suma = 0
while N > M:
    N = int(input("Ingresa el valor del numero en el que deseas empezar: "))
    M = int(input("Ingresa el valor del numero en el que deseas empezar: "))

    if M > N:
        for i in range(N + 1, M, 1):
            print(i)
            Suma = Suma + i
    else:
        print("El valor de N es mayor a M, por favor vuelva a ingresar los valores")

print("La suma de los numeros naturales contenidos entre el", N, "y el", M, "es", Suma)