from random import randint

arregloA = []
pares = []
i = 0

# Generar el arreglo A
while i <= 100:
    arregloA.append(randint(0,500))
    i+=1

# Mostrar numero pares
for x in range(0, len(arregloA), 2):
    pares.append(x)

# Copia arreglo
arregloB = []

# Suma arreglo
sum = 0
for z in arregloA:
    op = z* 3
    arregloB.append(op)
    sum += op

print(f"Numeros Pares: {pares}\nNumero Mayor: {max(arregloA)}\
      \nIndice Numero Mayor: {arregloA.index(max(arregloA))}\
      \nNumero Menor: {min(arregloA)}\
      \nArreglo A multiplicado por 3: {arregloB}\
      \nSuma Arreglo B: {sum}\
      \nPromedio: {sum/len(arregloB)}")
