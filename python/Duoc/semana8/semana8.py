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
            return (f"\nTipo: {datos[z][0]}\n"
                    f"Patente: {datos[z][1]}\n"
                    f"Marca: {datos[z][2]}\n"
                    f"Precio: ${datos[z][3]:,.2f}\n"  
                    f"Nombre Dueño: {datos[z][7]}\n")
        z+= 1

    else:
        return "Vehiculo no encontrado"
def imprimir_certificados():
    patente = input("Ingrese la patente que desea buscar: ")
    z = 0
    while z < len(datos):
        if patente in datos[z]:
            return  (
                f"\nCertificado de Emisión de Contaminantes\n"
                f"Patente: {datos[z][1]}\n"
                f"Dueño: {datos[z][7]}\n"
                "\nCertificado de Anotaciones Vigentes\n"
                f"Patente: {datos[z][1]}\n"
                f"Dueño: {datos[z][7]}\n"
                "\nCertificado de Multas\n"
                f"Patente: {datos[z][1]}\n"
                f"Dueño: {datos[z][7]}\n"
                f"Monto Multa: {datos[z][4]}\n"  
                f"Fecha Multa: {datos[z][5]}\n" 
            )
        z+= 1

    return "Vehiculo no encontrado"

def salir():
    return exit()

def Ejecutar (opcion):
    global i
    if (opcion == "1"):
        tipo = input("Ingrese el tipo de auto: ")
        patente = input("Ingrese la patente: ")

        for x in datos:
            if patente in x:
                print(f"\nLa patente {patente} ya se encuentra registrada")
                print(f"REGISTRE UN NUEVO AUTO O FINALICE LA SOLICITUD\n")
                inicio()        # input("Ingrese la patente del auto: ")
        marca = input("Ingrese la marca del auto: ")
        while len(marca) > 18 or len(marca) < 3:
            marca = input("Ingrese la marca del auto: ")
        precio = int(input("Ingrese el precio del auto: "))
        while precio < (3871):
            precio = int(input("Ingrese el precio del auto: ")) 
        monto_multa = int(input("Ingrese el monto_multa de la multas: "))
        fecha_multa = input("Ingrese la fecha de la multa:")
        
        fecha_registro = input("Ingrese la fecha de registro: ")
        nombre_dueño = input("Ingrese el nombre del dueño: ")
        grabar(tipo, patente, marca, precio, monto_multa, fecha_multa,  fecha_registro, nombre_dueño)
        # grabar("Manual", "321", "Ford", 123000, 120301230312, "28/01/2023",  "28/01/2023", "ignacio")
        # grabar("Automático", "458", "Toyota", 54000, 850298509825, "15/03/2022", "15/03/2022", "maria")

        # grabar("Manual", "122", "FOrd", 123123, 123312321, "02/04/2022",  "02/04/2022", "Pedro pedro")

        return "\nAuto Registrado\n"  
    elif (opcion == "2"):
        return f"\nResultado de busqueda: {buscar()}\n"
    elif (opcion == "3"):
        print(imprimir_certificados())
      
        
    elif (opcion == "4"):
        i = 1
        print("\nFin del programa")
        exit()
    
i = 0

def inicio():
    while (i == 0):
        print("Bienvenido a la automotora Motor City, cual de las siguientes opciones desea selecionar\
          \n1.grabar\n2.buscar\n3.Imprimir Certificados\n4.salir")
        seleccionar = input("Ingrese la opción que corresponda a su requerimiento: ")
        print(Ejecutar(seleccionar))
    

inicio()