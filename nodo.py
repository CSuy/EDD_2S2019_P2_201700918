class Nodo_Lista(): #Nodo que sirve para la Lista doble enlazada
    def __init__(self, cadena):
        self.anterior = None
        self.siguiente = None
        self.valor = cadena

class Nodo_AVL():
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
