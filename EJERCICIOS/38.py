# 38.	Escribe un algoritmo o el respectivo diagrama de flujo que, dados dos números, 
# verifique si ambos están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false

print("Vamos a determinar si dos numeros estan el el rango entre 0 y 5") # Informacion para el usuario

Num1 = float(input("Ingrese el valor para el Primer número: "))
Num2 = float(input("Ingrese el valor para el Segundo número: "))

if Num1 >= 0 and Num1 <= 5 and Num2 >= 0 and Num2 <= 5:
    print(Num1, "y", Num2, "---> True")
else:
    print(Num1, "y", Num2, "---> False")



