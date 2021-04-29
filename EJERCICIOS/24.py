# Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) 
# de una venta, si esta es mayor o igual 150.000 aplicar un descuento del 5% 

print("Vamos a determinar el IVA(19%) de una venta y si esta es mayor o igual a 150.000 se le calculara el descuento de 5%")

Valor = int(input("Ingresa el valor de la venta en pesos colombianos: "))
IVA = Valor * 0.19
ValorIVA = Valor + IVA
Descuento = ValorIVA * 0.05
ValorDesc = ValorIVA - Descuento

if Valor >= 150000:
    print("El IVA de la venta es", IVA)
    print("El Descuento de la venta es", Descuento)
    print("El valor total de la venta con el IVA y el Descuento incluido es", ValorDesc)
else:
    print("El IVA de la venta es", IVA)
    print("El valor total de la venta con el IVA incluido es", ValorIVA)