# 1.	Solicitar al usuario que ingrese su dirección de correo electrónico. 
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".
def validar(email):
    caracterBuscado="@"
    emailValido = False
    for c in email:
        if c==caracterBuscado:
            return True
    return False
 
n = False
while n == False:
    direccion=input("Tu email: ") 
 
    if validar(direccion): 
        print("Dirección válida") 
        n == True
 
    else: 
        print("Dirección inválida") 
        n == False
        print("El correo es invalido debido a que no lleva la @ en el correo")
        print("Por favor vuelvalo a ingresar")