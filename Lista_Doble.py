from nodo import Nodo_Lista
import os
import json

class Lista_Doble():
    def __init__(self):
        self.primero = None
        self.tam = 0

    def estaVacia(self):
        return self.tam == 0
    
    def insertar(self, valor):
        nuevo=Nodo_Lista(valor)
        if self.estaVacia():
            self.primero=nuevo
            self.primero.siguiente=None
            self.primero.anterior=None
            self.tam = self.tam + 1
        else:
            temporal=self.primero
            while (temporal.siguiente!=None):
                temporal=temporal.siguiente
            temporal.siguiente=nuevo
            nuevo.siguiente=None
            nuevo.anterior=temporal
            self.tam = self.tam + 1

    def buscar(self, index):
        aux = self.primero
        for i in range(self.tam):
            if index == i+1:
                return aux.valor
            else:
                aux = aux.siguiente

    def graficar(self):
        archivo = "ListaDoble.jpg"
        a = open("ListaDobleEnlazada.dot","w")
        a.write("digraph lista{\n")
        a.write("node[shape = record];\n")
        a.write("nodonull1[label="+chr(34)+"null"+chr(34)+"];\n")
        a.write("nodonull2[label="+chr(34)+"null"+chr(34)+"];\n")
        temporal=self.primero
        con=0
        for g in range(self.tam):
            try:
                json_aux = temporal.valor
                x = json.loads(json_aux)
                a.write("nodo"+str(g)+" [label="+chr(34)+"{|("+str(x["PREVIOUSHASH"])+")|}"+chr(34)+"];\n")
                temporal=temporal.siguiente
            except Exception:
                print("")
        a.write("nodonull1->nodo0 [dir=back];\n")
        for h in range(self.tam-1):
                c=h+1
                a.write("nodo"+str(h)+"->nodo"+str(c)+" [dir=both];\n")
                con=c
        a.write("nodo"+str(con)+"->nodonull2;\n")
        a.write("}")
        a.close()
        os.system("dot -Tjpg ListaDobleEnlazada.dot -o "+archivo)
        os.system(archivo)