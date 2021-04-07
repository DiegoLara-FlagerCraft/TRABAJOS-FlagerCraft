while True:
    option = input("""Elije una fruta para tu desayuno:
    1 - Manzanas
    2 - Bananas
    3 - Nada
    """)
    if option == "1":
        print("Has seleccionado Manzanas")
        break
    elif option == "2":
        print("Has seleccionado Bananas")
        break
    elif option == "3":
        print("Has seleccionado nada")
        break
    else:
        print("Debes seleccionar una opcion (1, 2 o 3)")
print("Programa terminado, que disfrutes tu desayuno :)")