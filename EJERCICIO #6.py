# Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen
# en esa frase (sin repetirlas).

Frase = input("Ingrese una frase: ")
Vocales = "AEIOUaeiou"
for d in Vocales:
    if d in Frase:
        print("Las vocales que utilizo en la frase son: ", d)