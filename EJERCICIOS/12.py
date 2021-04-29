# Escribe un algoritmo o el respectivo diagrama de flujo que determine la distancia recorrida por
# un objeto luego de una cantidad de tiempo, si se sabe que va en línea recta y además se conoce su 
# aceleración y su velocidad. 

import time
import os # Aspecto mas estetico

# Informacion para el Usuario
print("Vamos a calcular la distancia recorrida por un objeto despues de cierto tiempo a cierta velocidad y aceleracion. \n"
"Todo se va a calcular en m/s, metros y segundos. Todo lo anterior en base a la teoria del Movimiento Rectilineo Uniformemente Acelerado")

time.sleep(11)
os.system("cls")

t = int(input("Ingresa la cantidad de tiempo que demora el objeto en llegar a su destino en segundos: "))
a = int(input("Ingresa la aceleracion con la que recorre el objeto su trayecto en unidades de m/s cuadrados: "))
v = int(input("Ingresa la velocidad con la que parte el objeto en m/s: "))
d = (v * t + (a * (t ** 2)) / 2)

print("La distancia que recorre el objeto en",t, "segundos con una velocidad de", v, "m/s y una aceleracion de", a, "m/s cuadrados es", d, "metros")