#10.Escribir una función que, dada una cadena, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.  
# Consulta sobre la función len() en Python.

def ultimaPalabra(cadena): 
   if len(cadena)==0: 
       return 0 
   cantidad=0 
   for i in range(len(cadena)): 
       if cadena[i]!=' ': 
           cantidad+=1 
       else: 
           if i<len(cadena)-1 and cadena[i+1]!=' ': 
               cantidad=0 
   return cantidad 
cadena = input("Ingrese la cadena o frase = ") 
if ultimaPalabra(cadena): 
    print(ultimaPalabra(cadena)) 