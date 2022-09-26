#Sumar n cantidad de notas
notas = []

cant = int(input("Cuantas notas: "))

cont =0
while cont < cant:
    nota = int(input("Escriba la nota: "))
    notas.append(nota)
    cont += 1

suma = 0
for nota in notas:
    suma+=nota

print("La suma es ", suma)