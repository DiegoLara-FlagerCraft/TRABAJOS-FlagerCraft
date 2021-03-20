# Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci.
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números
# anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

NumeroAnt = 0
NumeroNue = 1
Fibonacci = 0
print(NumeroAnt)
print(NumeroNue)
for x in range(1, 9, 1):
    Fibonacci = NumeroAnt + NumeroNue
    NumeroAnt = Fibonacci - NumeroAnt
    NumeroNue = Fibonacci
    print(Fibonacci)