# 33.	Escribe un algoritmo o el respectivo diagrama de flujo que permita resolver una ecuación 
# cuadrática de tipo ax2 + bx + c (tenga en cuenta las todas las raíces, tanto las reales como las complejas).

print("Vamos a resolver una ecuación cuadrática de tipo ax2 + bx + c, Los resultados se daran en decimal")

a = float(input("Ingresa un valor para a: "))
b = float(input("Ingresa un valor para b: "))
c = float(input("Ingresa un valor para c: "))

FC1 = (-b + (((b ** 2) - 4 * a * c) ** 0.5)) / (2 * a)
FC2 = (-b - (((b ** 2) - 4 * a * c) ** 0.5)) / (2 * a)

print("Las dos posibles soluciones de la ecuación cuadratica son --- ", FC1, "y", FC2)