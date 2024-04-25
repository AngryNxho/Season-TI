datos = []
contador = 0
def grabar(*args):
    vehiculo = list(args)
    datos.append(vehiculo)
    

def buscar():
    patente = input("Ingrese la patente que desea buscar: ")
    z = 0
    while z < len(datos):
        if patente in datos[z]:
            print(datos[z])
            return f"\nTipo: {datos[z][0]}\nPatente: {datos[z][1]}\nMarca: {datos[z][2]}\nPrecio: {datos[z][3]}\nMonto Multa: {datos[z][4]}\nFecha Multa: {datos[z][5]}\nFecha Registro:\n{datos[z][6]}\nNombre Dueño: {datos[z][7]}"
        z+= 1
    # print(datos[indice])
def imprimir_certificados(certificado, anotaciones, multas):
    return None

def salir():
    return exit()

def Ejecutar (opcion):
    global i
    if (opcion == "1"):
        tipo = "Automatico" 
        # input("Ingrese el tipo de auto: ")
        patente = "123" 
        # input("Ingrese la patente: ")

        # print(f"Esta patente en Datos `{patente in datos}")
        for x in datos:
            if patente in x:
                print(f"\nLa patente {patente} ya se encuentra registrada")
                print(f"REGISTRE UN NUEVO AUTO O FINALICE LA SOLICITUD\n")
                reinicio()        # input("Ingrese la patente del auto: ")
        marca = "BWM"
        # input("Ingrese la marca del auto: ")
        while len(marca) > 18 or len(marca) < 3:
            marca = input("Ingrese la marca del auto: ")
        precio = 2222222 
        # int(input("Ingrese el precio del auto: "))
        while precio < (3871):
            precio = int(input("Ingrese el precio del auto: ")) 
        # int(input("Ingrese el precio del auto: "))
        # multas = "no" 
        monto_multa = 20000 
        # int(input("Ingrese el monto_multa de la multas: "))
        fecha_multa = "17/03/2022"
        # input("Ingrese la fecha de la multa:")
        
        fecha_registro = "20/09/2012" 
        # input("Ingrese la fecha de registro: ")
        nombre_dueño = "Gabriel"
        # input("Ingrese el nombre del dueño: ")
        # grabar(tipo, patente, marca, precio, monto_multa, fecha_multa,  fecha_registro, nombre_dueño)
        grabar("Manual", "321", "Ford", 123000, 120301230312, "28/01/2023",  "28/01/2023", "ignacio")
        grabar("Automático", "458", "Toyota", 54000, 850298509825, "15/03/2022", "15/03/2022", "maria")

        # grabar("Manual", "122", "FOrd", 123123, 123312321, "02/04/2022",  "02/04/2022", "Pedro pedro")

        return "\nAuto Registrado\n"  
    elif (opcion == "2"):
        return f"\nse han encontrado los siguientes datos: {buscar()}\n"
    elif (opcion == "3"):
        print("opcion 3")
      
        
    elif (opcion == "4"):
        i = 1
        print("\nFin del programa")
        exit()
    
i = 0

def reinicio():
    while (i == 0):
        print("Bienvenido a la automotora Motor City, cual de las siguientes opciones desea selecionar\
          \n1.grabar\n2.buscar\n3.Imprimir Certificados\n4.salir")
        seleccionar = input("Ingrese la opción que corresponda a su requerimiento: ")
        print(Ejecutar(seleccionar))
    

reinicio()