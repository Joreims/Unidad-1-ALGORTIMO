#Leer una cadena e imprimir letra por letra dicha cadena
import time
frase = input("Dime una frase: ")
for letra in frase:
    time.sleep(3)
    print(letra)
