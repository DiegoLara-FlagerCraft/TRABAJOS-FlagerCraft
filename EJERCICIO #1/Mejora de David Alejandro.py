#Especificar las variables, para evitar confusión al mirar el codigo después y que sea fácil la interacción con el usuario.

Tamaño = int(input("Ingrese cuántos valores quiere ver: ")) #Array
Multiplo = int(input("Ingrese el número que será el multiplo de los valores que quieres ver: "))
Multiplos = [] #Lista para guardar los multiplos para facilidad

for num in range(1, Tamaño+1): #Rango de 1, hasta los valores ingresados +1
    Multiplos.append(num*Multiplo) #Multiplica cada valor del rango por el multiplo ingresado 
print("Los", Tamaño, "multiplos de", Multiplo, "son:", Multiplos)