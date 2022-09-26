#Leer los datos de un estudiante como su nombre, carrera y promedio

#Crear clase Estuidante
import time

class Estudiante:
    def __init__(self, nom, car, prom):
        self.nombre = nom
        self.carrera = car
        self.promedio = prom

listEst = []

def agregarEst(nom, car, prom):
    try:
        est = Estudiante(nom, car, prom)
        listEst.append(est)
    except Exception as ex:
        print(str(ex))
        return 0
    return 1

def mostrarEst():
    print("*" *30)
    for est in listEst:
        print("Nombre: ", est.nombre)
        print("Carrera: ", est.carrera)
        print("Promedio: ", est.promedio)
        print("*" *30)

def principal():
    cant = int(input("Cuantos Estudiantes: "))
    cont = 0
    while(cont < cant):
        nom = input("Nombre: ")
        car = input("Carrrera: ")
        prom = float(input("Promedio: "))
        b = agregarEst(nom, car, prom)
        if( b == 1): print("Registro guardado...")
        else: print("Error al guardar...")
        cont += 1

    print("Voy a mostrar los registros guardado...")    
    time.sleep(2)
    mostrarEst()

principal()