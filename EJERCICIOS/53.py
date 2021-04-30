# 53.	Construye un algoritmo y el respectivo diagrama de flujo que permita leer una cantidad variable de números 
# indicando finalmente lo siguiente:
# • cuántos números fueron positivos
# • cuántos fueron negativos
# • cuantos fueron pares
# • cuantos fueron impares
# • cuántos fueron múltiplos de ocho

ContPos = 0
ContNeg = 0
ContPar = 0
ContImp = 0
ContMul8 = 0

N = int(input("¿Cuantos numeros deseas ingresar? = "))

for i in range(1, N + 1, 1):
    N = float(input("Ingresa un numero: "))
    if N > 0:
        ContPos = ContPos + 1
    if N < 0:
        ContNeg = ContNeg + 1
    if N % 2 == 0:
        ContPar = ContPar + 1
    if N % 2 != 0:
        ContImp = ContImp + 1
    if N % 8 == 0:
        ContMul8 = ContMul8 + 1

print(ContPos, "numeros fueron Positivos")
print(ContNeg, "numeros fueron Negativos")
print(ContPar, "numeros fueron Pares")
print(ContImp, "numeros fueron Impares")
print(ContMul8, "numeros fueron Multiplos de 8")