# 6.Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%)
#  de una venta realizada, indicando el valor original, el valor del IVA y el valor de la venta con IVA incluido.
print("Vamos a calcular el IVA de la venta de un producto")
IVA = 0.19
Valor = int(input("Ingresa el valor del producto que se va a vender: "))
ValorIVA = Valor * IVA
ValorFin = Valor + ValorIVA
print("El Valor original del producto es:", Valor)
print("El Valor del IVA es:", ValorIVA)
print("El Valor de la venta con IVA incluido es:", ValorFin)