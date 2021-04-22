# Si un array va a contener muchos más datos, puede resultar incómodo eso 
# de dar los valores iniciales uno por uno, y quizá no podamos emplear ".append" 
# si los valores no los vamos a recibir exactamente en orden. En ese caso, 
# se puede inicializar el array usando una orden "for" dentro de los corchetes, así: 

datos = [0 for x in range(10)] 
for i in range(0,len(datos)): 
    datos[i] = int( input( "Dime el dato numero {}: ".format(i+1) )) 
print ("Los datos al reves son: ") 

for i in range(len(datos),0,-1): 
    print ( datos[i-1] ) 

 