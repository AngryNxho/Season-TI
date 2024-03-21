
estreno = 4800
normal = 2900

palomitas_peq = 2500
palomitas_med = 4500
palomitas_gra = 7800

bebida_peq = 1000
bebida_med = 1250
bebida_gra = 2000

total_entradas = 0
total_palomitas = 0
total_bebidas = 0

validacion = input("¿Usted pertenece a la institución Duoc Uc? (Estudiante/Funcionario): ")
if validacion.lower() == "si":
    identificacion = input("Tiene usted la placa de identificación? ")
    if identificacion.lower() == "si":
        tiene_id = True
    else:
        tiene_id = False

    tipo_entrada = input(f"Normal: ${normal}\nEstreno: ${estreno}\nQué entrada desea comprar: ")
    print(tipo_entrada)
    if tipo_entrada.lower() == "estreno":
        total_entradas += estreno
    else:
        total_entradas += normal

    cantidad_entradas = int(input("Cuantas entradas desea comprar? "))
    total_entradas *= cantidad_entradas
    print(total_entradas)

    palomitas = input("¿Desea agregar palomitas a su compra? ")
    if palomitas.lower() == "si":
        print(f"Palomitas Pequeñas: ${palomitas_peq}\nPalomitas Medianas: ${palomitas_med}\nPalomitas Grandes: ${palomitas_gra}")
        tipo_palomita = input("Que tipo de Palomitas desea? ")
        if tipo_palomita.lower() == "palomitas pequeñas":
            total_palomitas += palomitas_peq
        elif tipo_palomita == "palomitas medianas":
            total_palomitas += palomitas_med
        else:
            total_palomitas += palomitas_gra

        can_palomita = int(input("Ingrese la cantidad de palomitas: "))
        total_palomitas *=  can_palomita

    agregar_bebida = input("Desea agregar bebidas: ")
    if agregar_bebida.lower() == "si":
        print(f"Bebida Pequeña: ${bebida_peq}\Bebida Mediana: ${bebida_med}\Bebida Grande: ${bebida_gra}")
        tipo_bebida = input("Ingresa el tamaño de la bebida: ")
        if tipo_bebida.lower() == "bebida pequeña":
            total_bebidas += bebida_peq
        
        elif tipo_bebida.lower() == "bebida mediana":
            total_bebidas += bebida_med

        else: 
            total_bebidas += bebida_gra

        can_bebida = int(input("Ingrese la cantidad de bebidas que desea: "))
    total_general = total_entradas + total_bebidas + total_palomitas     

    if tiene_id == True:
        total_general =  total_general - (total_general * 0.3)

    print(f"El total de su orden será ${int(total_general)}")
    pago_usuario = int(input("Ingrese el monto con el que va a pagar: "))
    print(f"Tiene un vuelto de ${pago_usuario - total_general}")
        
      