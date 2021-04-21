def Repeticion(Numeros,Digitos):
    Repet = Numeros.count(Digitos)
    return Repet

Numero = input("Ingrese un Número: ")
Digito = input("Ingrese el Dígito que desea saber que se repite: ")
print("La frecuencia del dígito en el número es:",Repeticion(Numero,Digito))
