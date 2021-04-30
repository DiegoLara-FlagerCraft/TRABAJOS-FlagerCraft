# 35.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número entre 0 y 10, imprima el nombre del número. 
# Ejemplo: 1 ---> UNO

print("Vamos a mostrar el nombre del número ingresado, el número debe estar entre 0 y 10") #Informacion para el usuaraio 

Num = int(input("Ingrese un número entre 0 y 10: "))
Nums = ["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","DIEZ"]
print("El nombre del numero", Num, "es", Nums[Num])
