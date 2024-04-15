from random import randint
arregloA = []
i = 0
# Crear arreglo
while i < 10:
    arregloA.append(randint(0,1000))
    i+= 1

# Numeros pares impares
contador_pares = 0
suma_impares = 0

for x in (arregloA):
    if x % 2 == 0:
        contador_pares+= 1
    else:
        suma_impares+= x

# primos 
primos = []


print(f"Elementos arreglo: {arregloA}\nCantidad de numeros pares: {contador_pares}\
      \nContador Impares: {suma_impares}\
      \nPrimo: {primos}")