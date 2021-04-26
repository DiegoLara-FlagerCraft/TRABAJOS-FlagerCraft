A = int(input("cuantos nombres de personas quieres ingresar? = "))
B = []
C = []
x=0
y=0
for i in range (0,A):
 B.append(input("Ingresa el nombre de una persona a la que quieras agregrar a la lista: "))
print ("estos son todos los nombres:",B)
for j in range (0,A):
 C.append(len(B[j]))
 print("el nombre",B[x],"tiene",C[y],"letras")
 x=x+1
 y=y+1