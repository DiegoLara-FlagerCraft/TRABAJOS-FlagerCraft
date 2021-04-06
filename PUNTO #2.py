# En una escuela se tienen tres tipos de calificaciones. Si el promedio escolar es mayor o igual a 7, 
# el estudiante es promovido; si está entre 4 o 7 es calificado como regular; si es menor a 4, el estudiante es reprobado. 
# Diseñar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima el mensaje correspondiente: 
# • Si el promedio es mayor o igual que 7 mostrar “Promocionado”. 
# • Si el promedio es menor o igual que 4 y mayor que 7 mostrar “Regular”. 
# • Si el promedio es menor que 4 mostrar “Reprobado”.

Nota1 = float(input("Ingrese la primera nota del estudiante: "))
Nota2 = float(input("Ingrese la segunda nota del estudiante: "))
Nota3 = float(input("Ingrese la tercera nota del estudiante: "))
Promedio = (Nota1 + Nota2 + Nota3)/3

if Promedio >= 7:
    print("PROMOCIONADO")
elif Promedio >= 4 and Promedio < 7:
    print("REGULAR") 
else:
    print("REPROBADO")