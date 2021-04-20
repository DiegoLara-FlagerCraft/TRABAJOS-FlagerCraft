# 3.El siguiente programa debería imprimir el número 2 si se le ingresan como valores 
# x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

def maximo(x,y):  
  if x>y:
    return x
  else:
    return y

 
def minimo(x,y):
  if x<y:
    return x
  else:
    return y

 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))