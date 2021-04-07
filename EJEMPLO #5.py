# 5.Al igual que la sentencia if, la estructura while también puede combinarse con una sentencia else.
total = 0
contar = 0
grado = int(input("mensaje: "))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input("mensaje: "))
else:
    promedio = total / contar
    print ("Promedio de notas del grado escolar: " + str(promedio))

