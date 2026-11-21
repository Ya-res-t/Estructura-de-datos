class Nodo: # Mi clase principal
    def __init__(self, dato): # Mi funcion dentro de mi clase
        self.dato = dato # Mi variable dentro de mi funcion
        self.siguiente = None # Puntero al siguiente nodo
class lista_enlazada:
    def __init__(self): # def solo define la funcion 
                        # el ini es un iniciador
        self.cabeza = None # El inicio de la lista en primer nodo empieza con 0 datos
    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos un nodo con el dato
        if self.cabeza is None: # Si el nodo esta vacio entonces entramos a la opcion verdadera
            self.cabeza = nuevo # Este nuevo nodo se convierte en el primero
            return
        actual = self.cabeza # Si ya hay nodos nos paramos en el primero o en la cabeza

        while actual.siguiente is not None: # Mientras haya unh nodo nos conectamos adelante
            actual = actual.siguiente # Caminar al siguiente nodo
        actual.siguiente = nuevo # Ya estando en el ultimo nodo, hacemos su apuntador señale al nuevo
        # Creamos la funcion y mostrar datos de la lista
    def imprimir (self):
        actual= self.cabeza # nos paramos en el primer nodo
        while actual is not None: # mientras haya un nodo
            print(actual.dato) # imprimimos el dato del nodo
            actual= actual.siguiente # nos movemos al siguiente nodo
        print("Fin de la lista")# cuando ya no haya nodos imprimimos que es el fin de la lista
# ahora imprimimos la lista enlazada
mi_lista = lista_enlazada() # creamos la lista vacia y le paso mi funcion de lista enlazada
mi_lista.insertar(10) # Insertamos el primer nodo con el dato 10
mi_lista.insertar(20)# Insertamos el primer nodo con el dato 20
mi_lista.insertar(30)# Insertamos el primer nodo con el dato 30
mi_lista.insertar(40)# Insertamos el primer nodo con el dato 40
mi_lista.imprimir() # mostramos los datos de la lista