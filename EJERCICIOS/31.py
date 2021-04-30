# 31.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el valor de un pasaje en avión, 
# conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer 
# es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%. 
# (el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000).

# Informacion para el usuario
print("Vamos a calcular cual es el precio Total de un pasaje de Avión teniendo en cuenta los km y los dias de estancia")

Distancia = int(input("Ingrese la distancia que va a recorrer en el vuelo en unidades de km: "))
Dias = int(input("¿Cuantos dias vas a estar en estancia? = "))
ValorMin = 100000
ValorKm = 5000
Valor = 0
Descuento = 0

if Distancia > 20: # Se coloca 20 porque es la cantidad de kilometros maxima para cobrar la tarifa estandar de 100.000 despues de 20km se cobra a 5000 por km
    Valor = Distancia * ValorKm
else:
    Valor = ValorMin

if Distancia > 1000 and Dias > 7:
    Descuento = Valor * 0.15
    Valor = Valor - Descuento

print("El Valor Total del pasaje de aviónn es: $" + str(Valor))