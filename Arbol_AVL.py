from nodo import Nodo_AVL

class Arbol():
    def __init__(self):
        self.root = None

    def estaVacia(self, raiz):
        return raiz == None

    def _insertar_AVL(self, raiz, cadena):
        if self.estaVacia(raiz):
            nuevo = Nodo_AVL(cadena)
            raiz = nuevo
        else:
            aux = raiz
            
        
    def insertar(self, datos):
        self._insertar_AVL(self.root, datos)