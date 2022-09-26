from time import sleep


class Libro:
    def __init__(self, tit, aut, edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi

    def __str__(self):
        return f"""Titulo: {self.titulo}
Autor: {self.autor}
Edición: {self.edicion}"""


pila = []


def menu():
    print("Pila")
    print("1. Ingresar ")
    print("2. Sacar")
    print("3. Mostrar")
    print("4. Salir")
    print("Digite la opcion")


def ingresarElemento():
    tit = input("Titulo: ")
    aut = input("Autor: ")
    edi = int(input("Edición en #: "))
    pila.append(Libro(tit, aut, edi))
    print("Libro apilado...")
    sleep(2)


def sacarElemento():
    libro = pila.pop()
    print(libro)
    print("Libro deapilado...")
    sleep(2)


def mostrarPila():
    print("Imprimiendo Pila")
    cima = len(pila)-1
    while(cima >= 0):
        print(pila[cima])
        cima -=1
    
 


def principal():
    try:
        op = 0
        while (op != 4):
            menu()
            op = int(input())
            if (op == 1):
                ingresarElemento()
            elif (op == 2):
                sacarElemento()
            elif (op == 3):
                mostrarPila()
            elif (op == 4):
                print("Adios")
            else:
                print("Opcion invalida....")

    except Exception as ex:
        print("Error:", str(ex))


principal()
