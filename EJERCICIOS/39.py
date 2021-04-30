# 39.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número del día de 
# la semana (entre 1 y 7) e indique el nombre del día. Por ejemplo:  1 ---> Lunes ; 5 ---> Viernes

print("Vamos a mostrar el nombre del dia de la semana a partir de su número") #Informacion para el usuaraio 

Dia = int(input("Ingrese un número entre 1 y 7: "))
Dias = ["EL FIN ESTA CERCA", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
print("El Dia de la semana correspondiente al numero", Dia, "es ---->", Dias[Dia])
