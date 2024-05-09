import os
import datetime
datos = []
contador = 0

def inicio():
    z = 0

    while z == 0:
        opciones = ["1", "2", "3", "4", "5"]
        print("Bienvenido a la línea aérea FalaFeria")
        opcion = input("¿Cuál de las siguientes opciones deseas realizar?\
                       \n1.Ver asientos_disponibles disponibles\
                       \n2.Comparar asiento\
                       \n3.Anular vuelo\
                       \n4.Modificar datos de pasasjero\
                       \n5.Salir\
                       \nSeleccione: ")
       
        while opcion not in opciones:
            print("Bienvenido a la línea aérea FalaFeria")
            opcion = input("¿Cuál de las siguientes opciones deseas realizar?\
                       \n1.Ver asientos_disponibles disponibles\
                       \n2.Comparar asiento\
                       \n3.Anular vuelo\
                       \n4.Modificar datos de pasasjero\
                       \n5.Salir\
                       \nSeleccione: ")

        if opcion == "1":
            print("Asientos disponibles", guardar_asientos)
        elif opcion == "2":
            print(comprar_asiento())
            global contador
            contador += 1
        
        elif opcion == "3":
            print(anular_vuelo())

        elif opcion == "4":
            modificar_datos()
        elif opcion == "5":
            print(salir())
            exit()
        
        


def asientos_disponibles():

    disponibles = [1, 2, 3, 4, 5, 6, 
                   7, 8, 9, 10, 11, 12
                   , 13, 14, 15, 16, 17
                   , 18, 19, 20, 21, 22
                   , 23, 24, 25, 26, 27
                   , 28, 29, 30, 31, 32
                   , 33, 34, 35, 36, 37
                   , 38, 39, 40, 41, 42
                   , 43, 44, 45, 46, 47, 48]
    print("Asientos disponibles")
    return disponibles

guardar_asientos = asientos_disponibles()
def comprar_asiento():
    valor_pago = 0
    descuento = 0
   
    numero_asiento = int(input("\nSeleccione el numero de su asiento: "))
    # print(guardar_asientos)

    while numero_asiento < 1 or numero_asiento > 48 or guardar_asientos[numero_asiento - 1] == "X":
        if numero_asiento < 1 or numero_asiento > 48:
            print("Debe escoger un número del 1 hasta el 48.")
        else:
            print("El asiento seleccionado está ocupado.")
        numero_asiento = int(input("\nSeleccione un número de asiento que no se encuentre ocupado: "))




        
    
    if numero_asiento <= 30:
        valor_pago = 180200

    else:
        valor_pago = 380000

    nombrePasajero = input("Ingrese su nombre y su dos appelidos: ")
    rut_pasajero = input("Ingrese su Rut: ")

    telefono_pasajero = input("Ingrese su telefono:  ")

    banco_pasajero = input("Ingrese su banco: ")
    if banco_pasajero.lower() == "bancoduoc":
        descuento = (valor_pago * 15) / 100

    usuario = [nombrePasajero, rut_pasajero, telefono_pasajero, banco_pasajero]
    datos.append(usuario)



    
    indice_asientos = asientos_disponibles().index(numero_asiento)  
    print(indice_asientos)
    if indice_asientos <= 31:
        valor = 180200
    else:
        valor = 380000

    
    guardar_asientos[numero_asiento - 1] = "X"

    print(descuento)
    return f"El valor de el Asiento: {numero_asiento} es de ${int(valor_pago - descuento)}"

def anular_vuelo():
    obtener_datos = int(input("Ingrese el numero de asiento que usted compró: "))
    guardar_asientos[obtener_datos - 1] = obtener_datos
    return f"El asiento {obtener_datos} ha sido liberado"

def modificar_datos():
    asiento = input("\nIngrese su numero de asiento: ")
    z = 0 
    rut = (input("Ingrese su Rut: "))
    while z < len(datos):
        if rut in datos[z]:
            print(datos[z])
            if rut in datos[z]:
                opcion = input("\n1.Nombre Pasajero\n2.Telefono Pasajero\n¿Qué datos deseas modificar?")
                if opcion == "1":
                    datos[z][0] = input("Cambio de nombre, ingrese su nuevo nombre: ")
                    return f"Se ha actualizado su nombre"
                else:
                    datos[z][2] = input("Cambio de telefono, ingrese su nuevo telefono: ")
                    return f"Se ha actualizado su numero de telefono"
                    
        z+= 1
            

def salir():
    fecha = datetime.datetime.now()
    return f"Programa finalizado - Nombre:{datos    [0]} Fecha:{fecha.date()}"
    # La opción Salir del menú debe mostrar un mensaje de salida del sistema, su nombre, apellido y la fecha actual. 




print(inicio())