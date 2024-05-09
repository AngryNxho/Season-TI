from random import randint
arregloA = []
arregloB = []

for x in range(11):
    arregloA.append(randint(0,300))

for i in range(11):
   arregloB.append(randint(0,300))


sumaA = 0
sumaB = 0
for z in range(len(arregloA)):
    sumaA +=arregloA[z]
    sumaB +=arregloB[z]

print(f"La suma del arreglo A: es {sumaA} - La suma del arreglo B es: {sumaB}")
print(f"La suma de ambos arreglos es: {sumaA + sumaB}")