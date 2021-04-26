Valido = True # Se valida la condición para que se ejecute el ciclo while

import time # Un mejor aspecto visual
import os

# Informacion para el usuario
print("En el siguiente programa evaluaremos los multiplos de un numero y en la cantidad que usted desee") 
time.sleep(4) # Tiempo en pantalla
os.system("cls") # Borrar pantalla

while Valido == True: # Se ejecuta un ciclo While para que repita el programa cuantas veces el usuario desee
    Tamaño = int(input("Ingrese el tamaño del arreglo: ")) # Se toma el tamaño del arreglo al usuario
    Multiplos = int(input("Ingrese el número de múltiplos: ")) # Se toma el numero al cual se le evaluaruan los multiplos al usuario
    ListaMultiplos = [] # Se determina una lista para guardar los multiplos

    for i in range (1,Tamaño+1): #Rango de 1, hasta los valores ingresados +1
        ListaMultiplos.append(i*Multiplos) #Multiplica cada valor del rango por el multiplo ingresado
        print("Los", Tamaño, "multiplos de", Multiplos, "son:", ListaMultiplos) # Se imprimen los multuplos del numero 
                                                                                # ingresado por el usuario

# Se determina un nuevo valor para Valido para poder determinar la continuidad del programa
    Valido = input("Si desea ejecutar nuevamente el programa escriba la letra S, si no desea ejecutarlo mas precione enter: ")
    if Valido == "S":
        Valido = True
    else:
        Valido = False
