import time
import os

# Informacion para el Usuario
print("A continuacion se ejecutara un programa que almacenara tantos nombres como usted indique \n"
"y calculara cuantas letras tiene cada nombre ")

time.sleep(6) # Mejoras de tiempo y mejora visual
os.system("cls")

A = int(input("Ingresa la cantidad de nombres que deseas ingresar: ")) # Se determina el tamaño del arreglo con ayuda del usuario
B = []
C = []

x = 0
y = 0

for i in range (0,A): #Range agrega los nombres a la lista hasta el límite que se determina en la variable A.
    B.append(input("Ingresa el nombre de las personas: "))
print ("estos son todos los nombres:",B)

for j in range (0,A): #Range cuenta la cantidad de carácteres de cada valor ingresado determinado por la variable A.
    C.append(len(B[j]))
    print("el nombre",B[x],"tiene",C[y],"letras")
    x=x+1
    y=y+1