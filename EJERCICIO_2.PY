#Nuevo ejercicio listas dobles enlazadas
class Nodo:
    def __init__(self,dato):
        self.dato=dato # Guarda el dato del nodo
        self.siguiente = None # Apuntador siguiente
        self.anterior = None # Apuntador interior
class listaDoble:
    def __init__(self):
        self.inicio= None # Marca cual es el primer nodo
        self.final= None # Marca cual es el ultimo nodo

    def insertar_al_inicio(self,dato):
        nuevo = Nodo(dato) # Crear el nuevo nodo en la lista
        if self.inicio is None: # Si el nodo esta vacio
            self.inicio = nuevo # Opcion ture (el inicio toma el valor del nuevo)
            self.final = nuevo # (como la final toma el valor del nuevo)
        else:
            nuevo.siguiente = self.inicio # el nuevo agarra al quye era primero
            self.inicio.anterior=nuevo  # el viejo primero agarra al nuevo
            self.inicio = nuevo # Actulizamos datos

    def inserter_al_final(self,dato):
        nuevo= Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo # Opcion true (el inicio toma el valor del nuevo)
            self.final = nuevo

        else:
            self.final.siguiente = nuevo
            nuevo.anterior= self.final
            self.final= nuevo

    def imprimir(self):
            actual=self.inicio
            while actual is not None:
                print (actual.dato)

                actual=actual.siguiente
            print ("Fin del nodo")
# Imprimir

tren_nodo = listaDoble()
tren_nodo.inserter_al_final(10)
tren_nodo.inserter_al_final(20)
tren_nodo.insertar_al_inicio(30)
tren_nodo.imprimir()