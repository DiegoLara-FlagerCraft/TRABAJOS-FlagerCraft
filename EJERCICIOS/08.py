# 8.Escribe un algoritmo o el respectivo diagrama de flujo que calcule el área de un hexágono.

import math

print("Vamos a calcular el Area de un Hexágono Regular")
Lado = float(input("Ingrese la longitud de uno de los lados del Hexágono en cm: "))
Perimetro = Lado * 6
Apotema = math.sqrt(Lado ** 2 - (Lado / 2) ** 2)
Area = (Perimetro * Apotema) / 2
print("El Area del Hexágono Regular es:", Area)