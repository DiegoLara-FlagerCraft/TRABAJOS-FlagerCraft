# Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y 
# si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este. 

print("Vamos a determinar si un numero es mayor o igual a 10 y si es asi devolver el triple de este, de lo contrario la cuarta parte de este  ")

Num = int(input("Ingresa un numero entero: "))

if Num >= 10:
    Triple = Num * 3
    print("El triple del numero es", Triple)
else:
    Cuarta = Num / 4
    print("La cuarta parte del numero es", Cuarta)