# Escribe un algoritmo o el respectivo diagrama de flujo que dadas coordenadas x1,y1 y x2,y2 
# en el plano cartesiano calcule la distancia entre ellos (considere todos los valores positivos) 

print("Vamos a calcular la distancia entre dos puntos situados en el plano carteciano")

x = float(input("Ingresa el valor para x en el primer punto: "))
y = float(input("Ingresa el valor para y en el primer punto: "))
x1 = float(input("Ingresa el valor para x en el segundo punto: "))
y1 = float(input("Ingresa el valor para x en el segundo punto: "))

Distancia = ((x - x1) ** 2  + (y - y1) ** 2) ** 0.5

print("La distancia entre el punto", x,",", y, "y", x1,",", y1, "es", Distancia)