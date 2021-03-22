#  La Universidad del Valle requiere un programa que le permita conocer cómo califican 
# los estudiantes la comida de la cafetería central. Para ello definió una escala de 1 a 10 
# (1 denota horrible y 10 denota excelente). El programa debe ser capaz capturar la 
# calificación de cualquier número de estudiantes (no se sabe cuántos estudiantes se 
# encuestarán, así que cuando el encuestador ingrese la calificación de 0, se sabrá que la encuesta habrá concluido). 
# El programa deberá mostrar en su salida cuántos estudiantes fueron encuestados así 
# como el resumen de la encuesta como el promedio y cuál es la nota más alta dada y 
# la nota más baja dada en la encuesta efectuada.

Num = 0
Estudiantes = 0
NumMen = 0
NumMay =  0
NumAnt = 0
Sumatoria = 0
Promedio = 0
print("Ingrese la calificacion para la cafeteria central entre 1 y 10, 1 es horrible y 10 es excelente.")
Num = float(input(""))
NumAnt = Num
while Num != 0:
    if Num <= NumAnt:
        NumMen = Num
        NumAnt = NumMen
    else:
        if Num > NumAnt:
            NumMay = Num
            NumAnt = NumMay
    Sumatoria += Num
    Estudiantes +=1
    print("Ingrese la calificacion para la cafeteria central entre 1 y 10, 1 es horrible y 10 es excelente.")
    Num = float(input(""))
Promedio = Sumatoria / Estudiantes
print("Se encuestaron " + str(Estudiantes) + " Estudiantes")
print("El promedio de la encuesta es:", Promedio)
print("La calificacion mas baja registrada es:", NumMen)
print("La calificacion mas alta registrada es:", NumMay)