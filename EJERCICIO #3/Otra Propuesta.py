def sumaDigitos(numero):
    suma=0
    while numero!=0: 
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

while True:
    num=int(input("Número a procesar: "))
    if num != 0:
        print("Suma:",sumaDigitos(num))
        numcadena = str(num)
        print("Digitos", len(numcadena))
    else:
        print("Programa terminado")
        break
