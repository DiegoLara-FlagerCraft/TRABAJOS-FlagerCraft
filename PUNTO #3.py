Dia = int(input("Introduce un día de la semana (entre 1 y 7): "))
print("El día es ... ", end="")
if Dia == 1:
    print("Lunes")
elif Dia == 2:
    print("Martes")
elif Dia == 3:
    print("Miercoles")
elif Dia == 4:
    print("Jueves")
elif Dia == 5:
    print("Viernes")
elif Dia == 6 or Dia== 7:
    print("Festivo")
else:
    print("Incorrecto")
    