# Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) 
# de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s). 

# Informacion para el usuario 
print("Vamos a calcular la energia de un objeto a partir de su masa y la velocidad de la luz, esto se determina por medio de la famosa \n"
"formula de Einstein E = mc2")

m = float(input("Ingresa la masa del objeto en kg: "))
vl = 299792458
E = m * (vl ** 2)

print("La energia del objeto con masa de", m, "kg y con la velocidad de la luz de", vl, "m/s es", E, "Julios")