n = False
while n == False:
    direccion = input("Ingrese el Correo de Email = ")
    def validar(direccion):
        if direccion.find("@" and (".co" or ".com")) >= 0:
            print("Direccion Válida")
            n == True
        else:
            print("Direccion Inválida, Favor volver a ingresar el Correo de Email")
            n == False
    validar(direccion)
