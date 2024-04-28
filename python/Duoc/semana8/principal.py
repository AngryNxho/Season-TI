from funciones import grabar, buscar, imprimir_certificados, salir, inicio, datos

while True:
    guardar_funcion = inicio()
    if guardar_funcion  == "1":
        tipo = input("Ingrese el tipo de auto: ")
        patente = input("Ingrese la patente: ")

        for x in datos:
            if patente in x:
                print(f"\nLa patente {patente} ya se encuentra registrada")
                print(f"REGISTRE UN NUEVO AUTO O FINALICE LA SOLICITUD\n")
        marca = input("Ingrese la marca del auto: ")
        while len(marca) > 18 or len(marca) < 3:
            marca = input("Ingrese la marca del auto: ")
        precio = int(input("Ingrese el precio del auto: "))
        while precio < (3871):
            precio = int(input("Ingrese el precio del auto: ")) 
        monto_multa = int(input("Ingrese el monto multa de la multas: "))
        fecha_multa = input("Ingrese la fecha de la multa:")

        fecha_registro = input("Ingrese la fecha de registro: ")
        nombre_dueño = input("Ingrese el nombre del dueño: ")
        grabar(tipo, patente, marca, precio, monto_multa, fecha_multa,  fecha_registro, nombre_dueño)

    elif guardar_funcion== "2":
        print(buscar())


    elif guardar_funcion == "3":
        print(imprimir_certificados())


    else:
        salir()





    