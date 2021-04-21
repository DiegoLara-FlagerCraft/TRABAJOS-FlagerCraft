x = 0
a = 0
t = 1
z = 1
x = int(input("Digite el número para generar los numero primos: "))

while t <= x:
    a = 0
    z = 1 
    while z <= t:
        if t % z == 0:
            a = a + 1
        z = z + 1
    if a == 2:
        print(t)
    t = t + 1
