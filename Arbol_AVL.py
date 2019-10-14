from nodo import Nodo_AVL

class Arbol():
    def __init__(self):
        self.root = None

    def estaVacia(self):
        return self.root == None

    def insertar_AVL(self, raiz):