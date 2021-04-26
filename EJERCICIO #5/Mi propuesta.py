import string
Alfabeto = list(string.ascii_lowercase)
for i in range(len(Alfabeto), 1, -1):
    if i % 3 == 0:
        Alfabeto.pop(i - 1)
print(Alfabeto)
