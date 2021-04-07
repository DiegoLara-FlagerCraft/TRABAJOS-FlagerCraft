# En este ejemplo tiene un contador con un valor inicial de cero,
# cada iteración del while manipula esta variable de manera que incremente su valor en 1, 
# por lo que después de su primera iteración el contador tendrá un valor de 1, luego 2, y así sucesivamente.
numero = 0
suma = 0
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
    print ("La suma es " + str(suma))
