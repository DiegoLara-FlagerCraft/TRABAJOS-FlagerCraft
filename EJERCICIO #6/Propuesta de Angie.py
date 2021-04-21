def factorial(numero): 
   f=1 
   if numero!=0: 
       for i in range(1,numero+1): 
           f=f*i 
   return f 
cantidad=0 
num=int(input("Ingrese un número e ingrese el -1 para dejar de ejecutar: ")) 
while num!=-1: 
    print("El número factorial de" + " " + str(num) + " es = " + str(factorial(num))) 
    cantidad+=1 
    num=int(input("Ingrese un número e ingrese el -1 para dejar de ejecutar: ")) 
print("Se leyeron",cantidad,"números") 
