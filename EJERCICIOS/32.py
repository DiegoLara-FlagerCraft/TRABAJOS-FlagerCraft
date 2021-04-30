# 32.	Escribe un algoritmo o el respectivo diagrama de flujo que permita determinar si un año dado es o no bisiesto.

print("Vamos a determinar si un Año es Bisiesto o no") # Informacion para el usuario

Año = int(input("Ingresa un año para determinar si es bisiesto o no: "))

if Año % 4 == 0 or Año % 400 == 0 or Año % 100 == 0:
    print("El año ingresado es Bisiesto")
else:
    print("El año ingresado no es Bisiesto")