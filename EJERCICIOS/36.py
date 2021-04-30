# 36.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número menor a un 100.000 
# determine la cantidad de dígitos que tiene. Por ejemplo 1093 tiene 4 dígitos.

print("Vamos a determinar cuantos digitos tiene un número menor a 100.000") # Información para el usuario

Num = int(input("Ingresa un numero entero menor a 100000: "))
cantidad = len(str(Num))
print("El numero",Num, "tiene", cantidad, "digitos")
