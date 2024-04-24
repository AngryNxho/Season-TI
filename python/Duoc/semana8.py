datos = []
def grabar(*args):
    for x in args:
        datos.append([x])
    return datos

def buscar():
    return datos


def imprimir_certificados(certificado, anotaciones, multas):
    return None

def salir():
    return exit()

def Ejecutar (opcion):
    global i

    if (opcion == '1'):
        tipo = 'Automatico'
        # input("Ingrese el tipo de auto: ")
        patente = '231jkla'
        # input("Ingrese la patente del auto: ")
        marca = "Mercedes"
        while len(marca) > 18 or len(marca) < 3:
            marca = input("Ingrese la marca del auto: ")
        precio = 200000
        while precio < 3871:
            precio = int(input("Ingrese el precio del auto: ")) 
        # int(input("Ingrese el precio del auto: "))
        multas = 2
        # input("Ingrese multas:  ")
        fecha_registro = '02/05/2024' 
        # input("Ingrese la fecha de registro: ")
        nombre_dueño = 'Pedro Gonzales'
        # input("Ingrese el nombre del dueño: ")
        grabar(tipo, patente, marca, precio, multas, fecha_registro, nombre_dueño)
        return "\nAuto Registrado\n"  
    elif (opcion == '2'):
        return f"\nse han encontrado los siguientes datos: {buscar()}\n"
    elif (opcion == '3'):
        print("opcion 3")
      
        
    elif (opcion == '4'):
        i = 1
    
i = 0

while (i == 0):
    print("Bienvenido a la automotora Motor City, cual de las siguientes opciones desea selecionar\
          \n1.grabar\n2.buscar\n3.Imprimir Certificados\n4.salir")
    seleccionar = input("Ingrese la opción que corresponda a su requerimiento: ")
    print(Ejecutar(seleccionar))
    

