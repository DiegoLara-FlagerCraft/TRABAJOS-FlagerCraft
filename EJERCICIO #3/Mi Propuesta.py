import time
import os

# Información para el Usuario
print("A continuacion se ejecutara un programa que le solicictara las notas que saco en algunas materias y posteriormente \n"
"mostrara una lista con la materias y la nota que ingresaste")
time.sleep(8) #Arreglos de tiempo y visuales
os.system("cls")

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"] # Se introduce una lista con unas maetias academicas basicas
scores = [] # Se determina otra lista

for subject in subjects: # Ciclo que permite pedir la nota a todas las metirias intriducidas en la lista
    score = input("¿Qué nota has sacado en " + subject + "? = ") # Se le solicita al usuario la nota obtenida en cada materia
    scores.append(score) # Se agregas a la lista de notas las notas ingresadas por el ususario

for i in range(len(subjects)): # Devuelve la lista de las materias
    print("En " + subjects[i] + " has sacado " + scores[i]) # Se muestra al usuario la materia y la nota que ingreso