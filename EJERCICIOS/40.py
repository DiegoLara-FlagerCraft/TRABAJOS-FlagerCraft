# 40.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al menos 2 de ellos son iguales 

print("Vamos a determinar si al ingresar 3 numeros al menos 2 son iguales") # Informacion para el usuario

Num1 = float(input("Ingresa el valor para el Primer número: "))
Num2 = float(input("Ingresa el valor para el Segundo número: "))
Num3 = float(input("Ingresa el valor para el Tercer número: "))

if Num1 == Num2 and Num1 == Num3:
    print("Todos los números son iguales")
elif Num1 == Num2:
    print("El primer número (", Num1, ") y el Segundo número (", Num2, ") son iguales")
elif Num1 == Num3:
    print("El primer número (", Num1, ") y el Tercer número (", Num3, ") son iguales")
elif Num2 == Num3:
    print("El Segundo número (", Num2, ") y el Tercer número (", Num3, ") son iguales")
else:
    print("Ningun número es igual")
    