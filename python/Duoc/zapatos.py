zapato = 20000
envio = 3000

cantidad  = int(input("Ingrese la cantidad de zapatos que desea comprar: "))
total = cantidad * zapato
if (total >= 40000):
    envio = 0


print(f"El total a pagar es de {total + envio}")