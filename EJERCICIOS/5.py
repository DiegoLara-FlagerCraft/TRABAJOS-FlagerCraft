# 5.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número decimal 
# e imprima su parte entera y su parte decimal por aparte.

print("Vamos a separar la parte entera y decimal de un numero decimal")
Num = float(input("Ingresa un numero decimal: "))
Entera = int(Num // 1)
Decimal = Num - Entera
print("La parte Entera de", Num, "es:", Entera)
print("La parte Decimal de", Num, "es:", Decimal)