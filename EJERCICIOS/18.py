# Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de 
# segundos indique cuántos horas minutos y segundos representan. Por ejemplo si el valor es 86399, 
# imprimirá el siguiente resultado -->  23:59:59 

print("A partir de unos segundos dados vamos a calcular a cuantas horas, minutos y segundos equivalen esos segundos")

s = int(input("Ingrese la cantidad de segundos: "))
seg = s % 60
seg1 = s // 60
minu = seg1 % 60
hor = seg1 // 60

print("Los", s, "segundos equivalen a", hor, ":", minu, ":", seg)