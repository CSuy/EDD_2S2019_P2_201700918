import csv
import json
import hashlib
import socket
import sys
import os
import time
import threading

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
                x = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                # convert into JSON:
                y = json.dumps(x)

# the result is a JSON string:
                print(y)
                print("area para seleccionar bloques")
            elif opcion == 3:
                print("area para realizar reportes")
            elif opcion == 4:
                print("Gracias :v")
                break

    def SHA_256(self,index1, timestamp1, class1, data1, previousH):
        bloque_analizado = str(index1).encode('utf-8') + str(timestamp1).encode('utf-8') + str(class1).encode('utf-8') + str(data1).encode('utf-8') + str(previousH).encode('utf-8')
        sha = hashlib.sha256(bloque_analizado).hexdigest()
        print("bloque analizado :v")
        print(bloque_analizado)
        return str(sha)

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
        #y=y.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
        #dd = json.loads(y)
        #index_ = str(dd["INDEX"])
        #timestamp_ = str(dd["TIMESTAMP"])
        #class_ = str(dd["CLASS"])
        #data_ = str(dd["DATA"]).replace('\'','\"').replace(' ','')
        #previous_ = str(dd["PREVIOUSHASH"])
        #hash_prueba = self.SHA_256(index_,timestamp_,class_,data_,previous_)
        #temporal = {"HASH": hash_prueba}
        #archivo_json.update(temporal)
        #json_final = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
        #print("El json final es este: \n" + json_final)   
inicio = Menu_Practica()
inicio.menu()
#180434