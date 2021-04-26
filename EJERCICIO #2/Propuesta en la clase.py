A = int(input("Ingresa el tamaño de los arreglos "))
B = []
C = []
for i in range (0,A):
 B.append(input("Ingresa el nombre de las personas "))
print (B)
for j in range (0,A):
 C.append(len(B[j]))
print (C)
