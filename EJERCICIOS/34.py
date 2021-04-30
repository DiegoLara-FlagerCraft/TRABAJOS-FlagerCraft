# 34.	Escribe un algoritmo o el respectivo diagrama de flujo que, dado un usuario y una contraseña 
# predefinida (por ejemplo usuario=”carlos" y contraseña=”1234”, le permita a un usuario digital su 
# usuario y contraseña y enviar un mensaje de inicio de sesión si lo digitado corresponde al usuario y contraseña predefinida.

print("Vamos a crear un usuario y contraseña y posteriormente iniciaremos sesión") # iNFORMACION PARA EL USUARIO

print("--------------> CREACIÓN <--------------")
Usuario = input("Cree un Usuario para su cuenta: ")
Contraseña = input("Cree una Contraseña para su cuenta: ")

print("\n \n--------------> INICIAR SESIÓN <--------------")
ValUsuario = input("Ingrese su Usuario: ")
ValContraseña = input("Ingrese su Contraseña: ")

# VALIDACIÓN
if Usuario == ValUsuario and Contraseña == ValContraseña:
    print("INICIO DE SESIÓN EXITOSO")
else:
    print("UPSS... AL PARECER EL USUARIO O LA CONTRASEÑA NO COINCIDE --- INICIO DE SESIÓN FALLIDO")

# SE PODRIA AÑADIR UN WHILE PARA QUE SE REPITA EL PROGRAMA HASTA QUE EL USUARIO Y LA CONTRASEÑA SEAN VALIDOS