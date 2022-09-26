import Clases as c

cola = c.Cola()
cod = 1

def menu():
    print("1. Agregar Cliente.")
    print("2. Atender Cliente")
    print("3. Mostrar Clientes")
    print("4. Salir")
    op = int(input("Escriba el # de la opcion: "))
    return op

def agregarClt():
    global cod
    nom = input("Nombres: ")
    ape = input("Apellidos: ")
    clt = c.Cliente(cod, nom, ape)
    cod +=1
    try:
        cola.agregar(clt)
    except Exception as ex:
        print(str(ex))
    
def atenderClt():
    print(cola.quitar())

def mostrarClt():
    for clt in cola.elementos:
        print(clt)

def main():
    op = 0
    while(op != 4):
        op = menu()
        if(op==1): agregarClt()
        elif(op==2): atenderClt()
        elif(op==3): mostrarClt()
        elif(op==4): print("Ciao, ciao...")
        else: print("Opcion invalida...")

main()

