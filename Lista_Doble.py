from nodo import Nodo_Lista

class Lista_Doble():
    def __init__(self):
        self.primero = None

    def estaVacia(self):
        return self.primero == None
    
    def insertar(self, cadena):
        nuevo = Nodo_Lista()
        if self.estaVacia():
            self.primero = nuevo
        else:
            temporal = self.primero
            while(temporal.siguiente != None):
                temporal = temporal.siguiente
            temporal.siguiente = nuevo
            nuevo.siguiente = None
            nuevo.anterior = temporal