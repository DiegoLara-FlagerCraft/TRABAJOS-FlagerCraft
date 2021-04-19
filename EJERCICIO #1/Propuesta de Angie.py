# 1.	Solicitar al usuario que ingrese su dirección de correo electrónico. 
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".
direccion = input("Ingrese el Correo de Email = ")
def validar(direccion):
    if direccion.find("@" and (".co" or ".com")) >= 0:
        print("Direccion Válida")
    else:
        print("Direccion Inválida")
validar(direccion)