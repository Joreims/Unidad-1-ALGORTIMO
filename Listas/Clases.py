#Crear una lista de estudiante
"""
Create
Read
Update
Delete
"""

class Estudiante:

    def __init__(self, cod, nom, ape, car, bec):
        self.Codigo = cod
        self.Nombres = nom
        self.Apellidos = ape
        self.Carrera = car
        self.Becado = bec #Becado sera un valor booleano
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Apellidos: {self.Apellidos}
Carrera: {self.Carrera}
Beca: {self.Becado}
"""

class ListadoEst:

    def __init__(self):
        self.lista =[]
    
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))
        
    def editarElemento(self, dato, pos):
        try:
            self.lista[pos]=dato
        except Exception as ex:
             print("Ocurrio un erro al editar:", str(ex))
    
    #def eliminarElemento(self, est) #Usar si deseo eliminar por su valor
    def eliminarElemento(self, pos): #Usar si deseo eliminar por su posicion
        try:
            #self.lista.remove(est) #Usar si deseo eliminar por su valor
            self.lista.pop(pos) #Usar si deseo eliminar por su posicion.
        except Exception as ex:
            print("Error al eliminar:", str(ex))
    
    def buscarElemento(self, codigo):
        try:
            pos = 0
            for est in self.lista:
                if est.Codigo == codigo:
                    print("Estudiante encontrado...")
                    return est, pos
                pos+=1
            else:
                print("No se encontro...")
            
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))
    


    

    

