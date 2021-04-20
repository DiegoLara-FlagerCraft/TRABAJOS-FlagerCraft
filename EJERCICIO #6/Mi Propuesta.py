# 6.Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(x, n):
    if(n > 0):
	    x = factorial(x, n-1)
	    x = x * n
    else:
        x = 1
    return x
    
cont = 0
Numero = int(input("Ingrese un numero para determinar su factorial (Para terminar digite el numero 0): "))
while Numero != 0:
    print("El factorial del numero ingresado es:", factorial(1, Numero))
    Numero = int(input("Ingrese un numero para determinar su factorial (Para terminar digite el numero 0): "))
    cont = cont + 1
print("Se leyeron",cont,"números")