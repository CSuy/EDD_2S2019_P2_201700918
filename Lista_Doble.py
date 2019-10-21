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
        temporal=self.primero
        for g in range(self.tam):
            try:
                json_aux = temporal.valor
                x = json.loads(json_aux)
                if(g+1==self.tam):
                    a.write("\"CLASS: " + str(x["CLASS"]) + "\n"+ "TIMESTAMP: " + str(x["TIMESTAMP"]) + "\n"+ "PREVIOUSHASH: " + str(x["PREVIOUSHASH"]) + "\n"+ "HASH: " + str(x["HASH"])  +"\";")
                else:
                    a.write("\"CLASS: " + str(x["CLASS"]) + "\n"+ "TIMESTAMP: " + str(x["TIMESTAMP"]) + "\n"+ "PREVIOUSHASH: " + str(x["PREVIOUSHASH"]) + "\n"+ "HASH: " + str(x["HASH"])  +"\" ->")
                temporal=temporal.siguiente
            except Exception:
                print("")
        a.write("}")
        a.close()
        os.system("dot -Tjpg ListaDobleEnlazada.dot -o "+archivo)
        os.system(archivo)

    def menu_bloques(self, index):
        aux = self.primero
        cadena = aux.valor
        if index != 1:
            for i in range(self.tam):
                if index == i+1:
                    cadena = aux.valor
                else:
                    aux = aux.siguiente
        listados = list(cadena)
        cadena_final = ""
        for j in range(150):
            cadena_final = cadena_final + listados[j]
        return cadena_final
        