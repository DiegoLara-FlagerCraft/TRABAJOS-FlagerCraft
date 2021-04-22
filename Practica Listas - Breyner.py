frase=["hola","mama","pollo","yuca"]
print(len(frase))
#prueba2##############################################################################
frase=["hola","mama","pollo","yuca"]
hola=int(input("ingrese un valor"))
frase.append(hola)
print(frase)
#################################################################################33333
#prueba3#################################################################################
#para agregar otro valor en la lista en la posicion que quiera, ya que el append solo agrega a lo ultimo
frase=["hola","mama","pollo","yuca"]
hola=int(input("ingrese un valor"))
frase.insert(2,hola)
print(frase)
#########################################################################################33
#para no agregar un solo elemento a la vez usamos extend
#prueba4
frase=["hola","mama","pollo","yuca"]
hola=int(input("ingrese un valor"))
frase.extend(["hola",hola,6,9])
print(frase)
############################################################################################33
#para sumar los valores de dos o mas listas
frase=["hola","mama","pollo","yuca"]
frase2=["hola","mama","pollo","yuca"]
frase3=frase+frase2
print(frase3)
##################################################################################################33
#saber si un determinado elemento esta en la lista
frase=["hola","mama","pollo","yuca"]
print(1 in frase)
##################################################################################################33
#contar cuantas veces se repite el valor de una lis
frase=["hola","mama","pollo","yuca,""hola","mama","pollo","yuca,"]
print(frase.count("mama"))
########################################################################################3
#eliminar valores de la lista por su indice
frase=["hola","mama","pollo","yuca"]
frase.pop(2)
print(frase)
#ejemplo w con pop
frase=["hola","mama","pollo","yuca"]
n=frase.remove(2)
print("lo que quiero comer yo es",n)
#eliminar valores de una lista por su nombre en si
frase=["hola","mama","pollo","yuca"]
frase.remove("hola")
print(frase)