import csv
import json
import hashlib
import socket
import sys
import os
import time
import threading
import select
from nodo import Nodo_AVL

class Menu_Practica():
    def menu(self):
        while True:
            print("----------Practica 2---------")
            print("1.Insertar Bloque")
            print("2.Seleccionar Bloque")
            print("3.Reportes")
            print("4.Cerrar Programa")
            opcion = int(input("Que opcion desea realizar... "))
            if opcion == 1:
                archivo_entrada = str(input("Ingrese el nombre del archivo con extension .csv...   "))
                self.insertarBloque(archivo_entrada)
                print("area de insertar bloques")
            elif opcion == 2:
                print("Este apartado es para seleccionar bloques")
            elif opcion == 3:
                print("area para realizar reportes")
            elif opcion == 4:
                print("Gracias :v")
                break
    
    def insertarBloque(self, archivo):
        lista = [] #creamos una lista temporal
        try:
            with open(archivo) as f:
                reader = csv.reader(f)
                for fila in reader:
                    lista.append(fila[0])
                    lista.append(fila[1])
        except Exception:
            archivo = ""
        lista1=lista[3].replace(' ','')
        archivo_json={
            "INDEX":2,
            "TIMESTAMP": "02-10-19-::14:30:25",
            "CLASS": lista[1],
            "DATA": lista1,
            "PREVIOUSHASH": "fd5f6d5fdfdf232Y232312QW12196255",
        }
        y = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
        y=y.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
        dd = json.loads(y)
        index_ = str(dd["INDEX"])
        timestamp_ = str(dd["TIMESTAMP"])
        class_ = str(dd["CLASS"])
        data_ = str(dd["DATA"]).replace('\'','\"').replace(' ','').replace("None","null")
        data_1 = data_
        datos = data_1.replace('\"value\"','').replace('right','').replace(':','')
        datos = datos.replace('left','').replace('\"','').replace(chr(123),'').replace(chr(125),'')
        alues = datos.split(',')
        previous_ = str(dd["PREVIOUSHASH"])
        hash_prueba = self.SHA_256(index_,timestamp_,class_,data_,previous_)
        temporal = {"HASH": hash_prueba}
        archivo_json.update(temporal)
        json_final = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
        print("El json final es este: \n" + json_final)
        print("")
        arbolito = arbol()
        for i in range(0,len(alues)):
            if alues[i] != "null":
                arbolito.insertar(alues[i])
        arbolito.Graficar()
        #arbolito.mostrar()
    

    def SHA_256(self,index1, timestamp1, class1, data1, previousH):
        bloque_analizado = str(index1).encode('utf-8') + str(timestamp1).encode('utf-8') + str(class1).encode('utf-8') + str(data1).encode('utf-8') + str(previousH).encode('utf-8')
        sha = hashlib.sha256(bloque_analizado).hexdigest()
        return str(sha)


class arbol():
    def __init__(self):
        self.root = None

    def insertar(self,dato):
        nuevo = Nodo_AVL(dato)
        if self.root is None:
            self.root = nuevo
        else:
            self._insertar1(self.root,nuevo)
    
    def _insertar1(self, raiz, datos):
        if raiz is None:
            raiz = datos
        else:
            if raiz.valor < datos.valor :
                raiz.izquierdo = self._insertar1(raiz.izquierdo,datos)
            else:
                raiz.derecho = self._insertar1(raiz.derecho,datos)
        return raiz

    
    def mostrar(self):
        valores = str(self._mostrar1(self.root.izquierdo))
        print(valores)

    def _mostrar1(self,raiz):
        if raiz is not None:
            return raiz.valor

    def Graficar(self):
        archivo = "Arbol.jpg"
        a = open("Arbol1.dot","w")
        a.write("digraph lista{\n")
        a.write("node [shape = circle, style=filled, fillcolor=seashell2];\n")
        a.write(self._graficar1(self.root))
        a.write(" \n}")
        a.close()
        os.system("dot -Tjpg Arbol1.dot -o"+archivo)
        os.system(archivo)
            

    def _graficar1(self,raiz):
        cuerpo = ""
        if(raiz is not None):
            cuerpo +="\""
            cuerpo += raiz.valor
            cuerpo +="\""
            cuerpo += ";"
            if raiz.izquierdo is not None :
                cuerpo +="\""
                cuerpo += raiz.valor
                cuerpo +="\""
                cuerpo += " -> \n"
                cuerpo += self._graficar1(raiz.izquierdo)
            if raiz.derecho is not None:
                cuerpo +="\""
                cuerpo += raiz.valor
                cuerpo +="\""
                cuerpo += " -> \n"
                cuerpo += self._graficar1(raiz.derecho)
        return cuerpo


inicio = Menu_Practica()
inicio.menu()