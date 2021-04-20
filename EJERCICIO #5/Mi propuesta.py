# 5.	Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, utiliza para ello una 
# función que calcule la frecuencia del dígito en el número ingresado.

def Repeticion(Numeros,Digitos):
    Repet = Numeros.count(Digitos)
    return Repet

Numero = input("Ingrese un Número: ")
Digito = input("Ingrese el Dígito que desea saber que se repite: ")
print("La frecuencia del dígito en el número es:",Repeticion(Numero,Digito))