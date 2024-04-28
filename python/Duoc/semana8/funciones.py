datos = []
def grabar(*args):
    vehiculo = list(args)
    datos.append(vehiculo)

def inicio():
    print("Bienvenido a la automotora Motor City, cual de las siguientes opciones desea selecionar\
          \n1.grabar\n2.buscar\n3.Imprimir Certificados\n4.salir")
    seleccionar = input("Ingrese la opción que corresponda a su requerimiento: ")

    return seleccionar

def buscar():
    patente = input("Ingrese la patente que desea buscar: ")
    z = 0
    while z < len(datos):
        if patente in datos[z]:
            return (f"\nTipo: {datos[z][0]}\n"
                    f"Patente: {datos[z][1]}\n"
                    f"Marca: {datos[z][2]}\n"
                    f"Precio: ${datos[z][3]}\n"  
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