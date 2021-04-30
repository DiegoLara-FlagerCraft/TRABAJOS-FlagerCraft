# 37.	Escribe un algoritmo o el respectivo diagrama de flujo que dados 3 números, determine si los números se están 
# incrementando, disminuyendo o ninguno de lo anterior de acuerdo con el orden de digitación. 
# Por ejemplo: 1 , 4, 19 --> está incrementando  ;  33, 10 ,1 --> está disminuyendo;   3 , 18 , 10 --> Ni se incrementa ni se disminuyendo

print("Vamos a determinar si al introducir tres numeros estos aumentan o disminuyen o no aumentan ni disminuyen") # Información para el Usuario

Num1 = float(input("Ingresa el valor para el Primer numero: "))
Num2 = float(input("Ingresa el valor para el Segundo numero: "))
Num3 = float(input("Ingresa el valor para el Tercer numero: "))

if Num1 < Num2 and Num2 < Num3:
    print("LOS NUMEROS ESTAN INCREMENTANDO")
elif Num1 > Num2 and Num2 > Num3:
    print("LOS NUMEROS ESTAN DISMINUYENDO")
else:
    print("LOS NUMEROS NO INCREMENTAN NI DISMINUYEN")