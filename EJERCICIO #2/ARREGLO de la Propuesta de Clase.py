# EJERCICIO 2

# def coordenadaZ(x,y):  # Esta parte del código no afecta a la ejecución del programa por lo que no hace falta conservarla
  # x=x+10
  # y=y+15
  # return x+y

 
#programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  # z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)
