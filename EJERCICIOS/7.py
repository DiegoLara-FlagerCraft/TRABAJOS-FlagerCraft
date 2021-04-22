# 7.Escribe un algoritmo o el respectivo diagrama de flujo que imprima el área y el perímetro de un círculo.

print("Vamos a calcular el Área y el Perímetro de un Círculo")
Pi = 3.1415
Radio = float(input("Ingresa el Radio del círculo en cm: "))
Area = Pi * (Radio ** 2)
Perimetro = (2 * Pi) * Radio
print("El Área del círculo es:", Area,)
print("El Perímetro del círculo es:", Perimetro,)