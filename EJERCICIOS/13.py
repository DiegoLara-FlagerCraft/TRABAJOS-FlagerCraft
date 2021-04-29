# Escribe un algoritmo o el respectivo diagrama de flujo que determine la velocidad final de un objeto luego de un tiempo, 
# si se sabe que va en línea recta y además se conoce su aceleración.

import time
import os # Aspecto mas estetico

# Informacion para el Usuario
print("Vamos a calcular la velocidad final de un objeto despues de cierto tiempo a cierta aceleracion y teniendo en cuenta que parte en reposo.\n"
"Todo se va a calcular en m/s, metros y segundos. Todo lo anterior en base a la teoria del Movimiento Rectilineo Uniformemente Acelerado")

time.sleep(11)
os.system("cls")

t = int(input("Ingresa la cantidad de tiempo que demora el objeto en llegar a su destino en segundos: "))
a = int(input("Ingresa la aceleracion con la que recorre el objeto su trayecto en unidades de m/s cuadrados: "))
v = 0
vf = (v + a * t)

print("La velocidad final con la que termina el objeto al trancurrir", t, "segundos y con una aceleracion de", a, "m/s cuadrados es", vf, "m/s")