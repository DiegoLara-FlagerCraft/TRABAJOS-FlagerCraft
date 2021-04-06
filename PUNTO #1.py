# En una institución se necesita de un programa que verifique que un número es múltiplo de 15. 
# Sin embargo, la máquina encargada de realizar el proceso solo puede aplicar el módulo a la entrada 
# sobre un número de un dígito. Debido a esto, se decidió que, para hallar el resultado, a la entrada se le 
# aplicarían módulo de 3 y módulo de 5, y si ambas respuestas eran correctas se sabría que el número es múltiplo de 15.
# Construya un programa que determine si el número ingresado por teclado es múltiplo de 3 y al mismo tiempo múltiplo de 5.

Num = int(input("Ingrese un Numero: "))
if Num % 5 == 0 and Num % 3 == 0:
    print("El numero es multiplo de 3 y de 5 al mismo tiempo")
else:
    print("El numero no es multiplo de 3 ni de 5 al mismo tiempo") 