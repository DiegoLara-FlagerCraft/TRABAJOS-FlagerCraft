# Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántas horas representan 

print("A partir de unos segundos dados vamos a calcular a cuantas horas equivalen esos segundos")

s = int(input("Ingrese la cantidad de segundos: "))
h = (s * 1/3600) #Convercion de unidades -----> en 1 hora hay 3600 segundos 
print("Los", s, "segundos quivalen a", h, "horas")