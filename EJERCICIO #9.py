# Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando
# todos los números enteros positivos que hay entre el 1 y ese número.

n = int(input("Ingrese un numero entero positivo: "))
Factorial = 1
for x in range(1, n+1, 1):
    Factorial = Factorial * x
print ("El factorial del numero " + str(n) + " es igual a:", Factorial)
