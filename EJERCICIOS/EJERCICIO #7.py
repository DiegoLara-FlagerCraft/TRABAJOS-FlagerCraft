# Y si la matriz es de un tamaño grande, puede ser más cómodo crearla y rellenarla de forma repetitiva, así: 

datos = [ [0 for columna in range(0,5)] for fila in range (0,4)] 
datos[0][2] = 5 
print(datos) 