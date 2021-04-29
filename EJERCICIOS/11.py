# 11.Escribe un algoritmo o el respectivo diagrama de flujo que determine el tiempo de caída de un objeto que se suelta desde una altura h.

import time
import os # Para generar una mejor interaccion con el usuario en cuestion de aspecto

# Informacion del usuario
print("Vamos a calcular el tiempo que demora un objeto en caer desde cierta altura, todo calculado en metros y segundos")
time.sleep(5)
os.system("cls")

h = int(input("Ingresa la altura desde donde va a ser lanzado el objeto en metros: "))
g = 10 # Tomamos la gravedad como 10 m/s al cuadrado
t = ((h * 2) / g) ** 0.5

print("El tiempo que se demora en caer el objeto desde los", h, "metros es", t, "segundos")