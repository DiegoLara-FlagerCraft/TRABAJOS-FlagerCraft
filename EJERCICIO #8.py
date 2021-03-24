# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese
# rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por
# 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

A1 = int(input("Ingresa cualquier año: "))
A2 = int(input("Ingresa otro año: "))
print("Los años Biciestos que se encuentran etre los años " + str(A1) + " y " + str(A2) + " son: ")
for n in range(A1, A2+1, 1):
    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        print(n)
print("Los años que son Multiplos de 10 que se encuentran etre los años " + str(A1) + " y " + str(A2) + " son: ")
for m in range(A1, A2+1, 1):
    if m % 10 == 0:
        print(m)
