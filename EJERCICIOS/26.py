# Escribe un algoritmo o el respectivo diagrama de flujo que lea las cinco notas obtenidas 
# por un estudiante y calcule su nota final, sabiendo que las cada nota tiene el siguiente valor: 
# n1 (15%), n2 (20%), n3 (15%), n4 (30%), n5 (20%). Si la nota obtenida es menor a 2,0 deberá indicarle 
# al estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es 
# mayor o igual a 3 deberá indicar que aprobó y si es mayor a 4,5 extenderá un mensaje de felicitación al estudiante. 

Nota1 = float(input("Ingrese la primera nota del estudiante entre 0 y 5: "))
Nota2 = float(input("Ingrese la primera nota del estudiante entre 0 y 5: "))
Nota3 = float(input("Ingrese la primera nota del estudiante entre 0 y 5: "))
Nota4 = float(input("Ingrese la primera nota del estudiante entre 0 y 5: "))
Nota5 = float(input("Ingrese la primera nota del estudiante entre 0 y 5: "))
P1 = 0.15
P2 = 0.2
P3 = 0.15
P4 = 0.3
P5 = 0.2
Promedio = (Nota1 * P1 + Nota2 * P2 + Nota3 * P3 + Nota4 * P4 + Nota5 * P5)

if Promedio < 2:
    print("NO PUEDE HABILITAR")
    print("SU PROMEDIO FUE", Promedio)
elif Promedio < 3:
    print("REPROBÓ") 
    print("SU PROMEDIO FUE", Promedio)
elif Promedio > 4.5:
    print("FELICITACIONES APROBO CON HONORES")
    print("SU PROMEDIO FUE", Promedio)
elif Promedio >= 3:
    print("APROBÓ")
    print("SU PROMEDIO FUE", Promedio)