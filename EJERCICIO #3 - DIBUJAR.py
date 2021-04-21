n = int(input("Ingresa un número: "))
i = 0
e = 0
b = 0
NumeroEspacios = n - 1
NumeroBaldosas = 1
for i in range(0, i < n, 1):
    for e in range(0, e < NumeroEspacios, 1):
        print(" ")
        e = e +1
    for b in range(0, b < NumeroBaldosas, 1):
        print("#")
        b = b + 1
    print("\n") #Mover carro a la siguiente linea
    NumeroEspacios = NumeroEspacios - 1
    NumeroBaldosas = NumeroBaldosas + 1
    i = i + 1
