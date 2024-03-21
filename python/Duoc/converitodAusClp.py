print("1. Dolar Australiano a Peso Chileno\n2. Peso Argentino a Peso Chileno\n3. Yen a Pesos Chilenos")
usuario = input("Ingrese la divisa que desea convertir: ")
dinero = eval(input("Ahora ingrese el dinero que desea convertir: "))

if usuario == "1":
    print(f"${dinero} Peso(s) Australiano(s) equivale a ${round(dinero * 637, 2)} Peso(s) Chilenos")

elif usuario == "2":
    print(f"${dinero} Peso(s) Argentino(s) equivale a ${round(dinero * 1.13, 2)} Peso(s) Chilenos")

else:
    print(f"${dinero} Yene(s) equivale a ${round(dinero * 6.39, 2)} Peso(s) Chilenos")
