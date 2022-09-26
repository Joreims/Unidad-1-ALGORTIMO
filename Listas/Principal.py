from Clases import Estudiante as est, ListadoEst as lst
from os import system
listaEst = lst()

def menu():
    system("cls")
    print("="*50)
    msn = f"Registros almacenados: {len(listaEst.lista)}"
    print(msn.center(50, " ") )
    print("="*50)
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Buscar por código")
    print("5. Mostrar Registros")
    print("6. Buscar por nombres")
    print("10. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarRegistro():
    print("Agregar Datos del Estudiante")
    codigo = input("Código: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): beca = True
    else: beca = False
    estudiante = est(codigo, nombres, apellidos, carrera, beca)
    print(estudiante)
    listaEst.agregarElemento(estudiante)
    print("Registro guardado...")
    system("pause")

def modificarRegistro():
    print("Editar Registro ")
    cod = input("Código: ")
    estOriginal, pos = listaEst.buscarElemento(cod)
    print("Datos del estudiante")
    print(estOriginal)
    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevoApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): nuevaBeca = True
    else: nuevaBeca = False
    newEst = est(cod, nuevoNombre, nuevoApellidos, nuevaCarrera, nuevaBeca)
    listaEst.editarElemento(newEst, pos)
    system("pause")

def eliminarRegistro():
    print("Eliminar Registro")
    cod = input("Código: ")
    estActual, pos = listaEst.buscarElemento(cod)
    print(f"""Realmente desea eliminar el registro {estActual}""")
    resp = input("SI - NO: ")
    if resp.upper()=="SI":
        listaEst.eliminarElemento(pos)
    else:
        print("Operación cancelada")
    system("pause")

def buscarRegistro():
    print("Buscar Registro")
    cod = input("Código: ")
    try:
        est, pos = listaEst.buscarElemento(cod)
 
        if est.Codigo != None:
            print(est)
    except:
        print("Todo bien segui adelante")
        
    
def mostrarRegistros():
    for estudiante in listaEst.lista:
        print(estudiante)
        print("="*30)
    system("pause")

def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: buscarRegistro()
        elif op == 5: mostrarRegistros()
        elif op == 10: print("Ciao, ciao")
        else: print("Opcion no valida")

main()