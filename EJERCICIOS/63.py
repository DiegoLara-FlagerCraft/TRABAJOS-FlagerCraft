# Un elefante decidió visitar a su amigo. Resultó que la casa del elefante está ubicada en el punto 0 
# y la casa de su amigo está ubicada en el punto x (x> 0) de la línea de coordenadas. En un solo paso, el elefante 
# puede avanzar 1, 2, 3, 4 o 5 posiciones. Determina cuál es el número mínimo de pasos que debe realizar para llegar a la casa de su amigo.

ContP = 0
Pisadas = int(input("¿En que punto esta ubicada la casa del amigo del elefante? = "))
if Pisadas <= 5:
    print("El elefanta tiene que realizar", 1, "pisada")
elif Pisadas > 5:
    while Pisadas > 0:
        Pisadas = Pisadas - 5
        ContP = ContP + 1 
    print("El elefante tiene que realizar", ContP, "pisadas para llegar a donde su amigo")

