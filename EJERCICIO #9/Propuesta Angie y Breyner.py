# 9.Escribir una función que, dado un número de cédula de ciudadanía, 
# retorne True si el número es válido y False si no lo es. Consulta cuál es la longitud válida para cédula en Colombia.

cond="si" 
def frecuencia(numero): 
	cantidad=0 
	while numero!=0: 
	    ultDigito=numero%10 
	    cantidad+=1 
	    numero=numero//10 
	return cantidad 
while cond=="si": 
	hi=input("""que desea ingresar: 
	1.Cedula de ciudadania 
	2.Tarjeta de identidad 
	 = """) 
	num=int(input("Ingrese el número: ")) 
	if frecuencia(num)< 4 and frecuencia(num)< 12: 
	    print("el numero  es invalido") 
	else: 
	    print("El número es valido.") 
	    cond="no" 
	cond=input("¿Quieres volver a ingresar? ¿si o no?= ") 
	if cond =="no": 
	    print("Vuelve pronto amigo…(saludos desde Bucaramanga y Tibú para el mundo).")       
#En colaboración de Breyner - Tibú 
