
fin = False
registros = [
    
]

# ["654321", 2012, 'p', 'volvo', 'xd'], 
    # ["987654", 2010, 'p', 'toyota', 'lol'], 
    # ["456789", 2010, 'p', 'toyota', 'lol'],
    # ["333444", 2015, 'p', 'ford', 'haha'], 
    # ["555666", 2015, 'p', 'ford', 'haha'],
    # ["111222", 2018, 'p', 'chevrolet', 'rofl'], 
    # ["999888", 2018, 'p', 'chevrolet', 'rofl'],
    # ["777888", 2020, 'p', 'honda', 'lmao'], 
    # ["222333", 2020, 'p', 'honda', 'lmao']
i = 0

while fin == False:
    # print(registros)

    print("\n1.Ingresar automóvil\n2.Registro de mantenimiento\n3.Consultar automóvil\n4.Salir")
    inicio = int(input("Selecciona cual de las opciones quieres realizar: "))

    if inicio == 1:
        patente = input("Ingrese la patente del vehículo: ")
        while len(patente) != 6 and patente not in registros:    
            patente = input("La patente debe contener 6 caracteres.\nIngrese nuevamente la patente del vehículo: ")
        if (len(patente ) == 6):
            for z in registros:
                if (z[0] == patente):
                    print(f"La patente {patente} ya se encuentra registrada.\nInicie nuevamente el proceso")
                    exit()
        registros.append([patente])
        print("Año de fabricación.\nFormatos disponibles AA1000/BBBB10")
        a_fabricacion = int(input("Ingrese el año de fabricación: "))

        while (a_fabricacion not in range(1980, 2024)):
            a_fabricacion = int(input("Error. Ingrese nuevamente el año de fabricación: "))
        registros[i].append(a_fabricacion)

        tipo_lista = ["p", "b", "e", "h"]
        tipo = input("Ingrese el tipo de vehículo: ")
        while tipo.lower() not in tipo_lista:
            tipo = input("Ingrese nuevamente el tipo de vehículo: ")    
        registros[i].append(tipo)

        marca = input("Ingrese la marca del vehículo: ")
        while len(marca) < 1:
            marca = input("Debe ingresar la marca del vehículo:")
        registros[i].append(marca)

        modelo = input("Ingrese el modelo del vehículo: ")
        while len(modelo) < 1:
            modelo = input("Debe ingresar el modelo del vehículo: ")
        registros[i].append(modelo)

        i+= 1
    if inicio == 2:
        patente = input("Ingrese la patente: ")
        for x in registros:
            if (x[0] == patente):
                fecha = input("Ingresar fecha: ")
                observaciones = input("Ingrese las observaciones: ")
                i-= 1
                registros[i].append(fecha)
                registros[i].append(observaciones)
                print(registros[i])

    if inicio == 3:
        patente = input("Ingrese la patente: ")

        for y in registros:
            if y[0] == patente:
                print(f"Y es {y}")