# Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos minutos representan 

print("A partir de unos segundos dados vamos a calcular a cuantos minutos equivalen esos segundos")

s = int(input("Ingrese la cantidad de segundos: "))
m = (s * 1/60) #Convercion de unidades -----> en 1 minuto hay 60 segundos 
print("Los", s, "segundos quivalen a", m, "minutos")