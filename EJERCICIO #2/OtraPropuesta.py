def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
        return suma

num = int(input("Digite números menores que 10 sin espacios entre sí, ni símbolos y estos serán sumados, para terminar digite 0: "))
while num != 0:
    print("Suma:", sumaDigitos(num))
    num = int(input("Digite números menores que 10 sin espacios entre sí, ni símbolos y estos serán sumados, para terminar digite 0: "))
