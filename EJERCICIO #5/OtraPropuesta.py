cond = "si"
def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == digito:
            cantidad += 1
        numero = numero // 10
    return cantidad

while cond == "si":
    num = int(input("Ingrese un número: "))
    un_digito = int(input("Ingrese un Digito: "))
    print("Frecuencia del dígito en el número:", frecuencia(num, un_digito))
    cond = input("quieres volver a ingresar un número y un digito, ¿si o no? ")
    if cond == "no":
        print("Vuelva pronto amigo....(saludos desde Tibú)")