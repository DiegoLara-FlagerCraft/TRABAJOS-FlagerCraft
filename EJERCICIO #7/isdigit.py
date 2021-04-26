print("Vamos a evaluar si el contenido que ingreses solo contiene numeros")
Valor = input("Ingresa algun contenido: ")
Result = Valor.isdigit()
if Result == True:
    print("El contenido es numerico")
else:
    print("El contenido no es netamente numerico")

