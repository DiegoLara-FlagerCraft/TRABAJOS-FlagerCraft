# 3.	Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados 
# y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

print("Vamos a Calcular la suma individual de los numeros que desees digitar y la suma total de dichos numeros hasta que ingreses el numero 0 ")
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

SumaTotal = 0
num = int(input("Número a procesar: "))
while num!=0:
    SumaTotal = SumaTotal + num
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))
print("La Suma de todos los digitos es:", SumaTotal)
print("La cantidad total de digitos ingresados fue:", sumaDigitos(SumaTotal))