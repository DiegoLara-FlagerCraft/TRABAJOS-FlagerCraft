Año = int(input("Ingrese un año para determinar si es bisiesto o no: "))
Bisiesto = False
if Año % 4 == 0 or Año % 100 == 0 or Año % 400 == 0:
        Bisiesto = True
if Bisiesto == True:
    print("El Año ingresado es Bisiesto")
else:
    print("El Año ingresado no es Bisiesto")