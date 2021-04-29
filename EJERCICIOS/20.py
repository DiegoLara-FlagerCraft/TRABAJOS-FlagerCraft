# Escribe un algoritmo o el respectivo diagrama de flujo que, dada un numero de 4 cifras, 
# reordene sus dígitos de manera inversa. Por ejemplo 3245 ---> 5423 

print("Vamos a reordenar un numero de 4 cifras de manera inversa")

Digito = input("Ingresa un digito de 4 cifras: ")
inverso = Digito[::-1] # Es “cortar” la cadena pero sin especificar inicio ni fin, solo especificando el step; de esta manera avanzamos de -1 en -1; invirtiendo la cadena.
print("El inverso de",Digito, "es", inverso)