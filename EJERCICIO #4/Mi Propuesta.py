# 4.Solicitar al usuario que ingrese un número entero e informarle si es primo o no, 
# utiliza en el código una función booleana que lo decida.

import time #Importar el tiempo
# Validar si es primo o no dividiendo por todos lo numeros desde 2 hasta llegar a el numero
def Primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

print("Este programa determina si un numero es Primo o No") #Informacion para el usuario
#Para que el usuario pueda seguir validando numeros
Seguir = 1
while Seguir != -0:
    N = int(input("Ingrese un numero para determinar si es Primo o No: "))
    if Primo(N):
        print("El numero Ingresado es Primo")
    else:
        print("El numero Ingresado no es Primo")

    time.sleep(2) #Esperar tiempo en segundos
    Seguir = int(input(("¿Quieres ingresar otro numero para determinar si es Primo o No? \n"
    "- Si deseas seguir digita 1 \n"
    "- Si no deseas seguir digita -0 \n")))