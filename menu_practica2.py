import csv
import json
import hashlib
import socket
import sys
import os
import time
import threading
import select
import msvcrt
from nodo import Nodo_AVL
from nodo import Nodo_Lista
from Lista_Doble import Lista_Doble
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import curses

lista_1 = Lista_Doble()
json_memoria = ""
json_arbol = ""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
def servidor():
    if len(sys.argv) != 3:
        print ("Correct usage: script, IP address, port number")
        exit()
    server.connect((IP_address, Port))
    while True:
	# maintains a list of possible input streams
        read_sockets = select.select([server], [], [], 1)[0]
        import msvcrt
        if msvcrt.kbhit(): read_sockets.append(sys.stdin)

        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                #print (message.decode('utf-8'))
                analisis_json(message.decode('utf-8'))
    server.close()

def menu():
    while True:
        os.system('cls')
        print("----------Practica 2---------")
        print("1.Insertar Bloque")
        print("2.Seleccionar Bloque")
        print("3.Reportes")
        print("4.Cerrar Programa")
        opcion = int(input("Que opcion desea realizar... "))
        if opcion == 1:
            #os.system('cls')
            archivo_entrada = str(input("Ingrese el nombre del archivo con extension .csv...   "))
            insertarBloque(archivo_entrada,server)
            print("area de insertar bloques")
        elif opcion == 2:
            seleccionar_bloques()
            print("Este apartado es para seleccionar bloques")
        elif opcion == 3:
            lista_1.graficar()
            print("area para realizar reportes")
        elif opcion == 4:
            print("Gracias :v")
            break

def insertarBloque(archivo, servidor1):
    global json_memoria
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
    if lista_1.estaVacia():
        archivo_json={
            "INDEX":lista_1.tam,
            "TIMESTAMP": time.strftime(("%d-%m-%y-::%H:%M:%S")),
            "CLASS": lista[1],
            "DATA": lista1,
            "PREVIOUSHASH": "0000",
        }
        y = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
        y=y.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
        dd = json.loads(y)
        index_ = str(dd["INDEX"])
        timestamp_ = str(dd["TIMESTAMP"])
        class_ = str(dd["CLASS"])
        data_ = str(dd["DATA"]).replace('\'','\"').replace(' ','').replace("None","null")
        previous_ = str(dd["PREVIOUSHASH"])
        hash_prueba = SHA_256(index_,timestamp_,class_,data_,previous_)
        temporal = {"HASH": hash_prueba}
        archivo_json.update(temporal)
        json_final = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
        json_memoria = json_final.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
        server.sendall(str(json_final).encode('utf-8'))
    else:
        try:
            json_prueba = lista_1.buscar(lista_1.tam)
            x = json.loads(json_prueba)
            archivo_json1={
                "INDEX":lista_1.tam,
                "TIMESTAMP": time.strftime(("%d-%m-%y-::%H:%M:%S")),
                "CLASS": lista[1],
                "DATA": lista1,
                "PREVIOUSHASH": str(x["HASH"]),
            }
            y1 = json.dumps(archivo_json1).replace("\\n",'').replace("\\",'')
            y1=y1.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
            dd1 = json.loads(y1)
            index_1 = str(dd1["INDEX"])
            timestamp_1 = str(dd1["TIMESTAMP"])
            class_1 = str(dd1["CLASS"])
            data_1 = str(dd1["DATA"]).replace('\'','\"').replace(' ','').replace("None","null")
            previous_1 = str(dd1["PREVIOUSHASH"])
            hash_prueba1 = SHA_256(index_1,timestamp_1,class_1,data_1,previous_1)
            temporal1 = {"HASH": hash_prueba1}
            archivo_json1.update(temporal1)
            json_final1 = json.dumps(archivo_json1).replace("\\n",'').replace("\\",'')
            json_memoria = json_final1.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
            server.sendall(str(json_final1).encode('utf-8'))
        except Exception:
            print("error al buscar el json")

def analisis_json(cadena):
        cadena1 = str(cadena)
        global json_memoria
        if cadena1.find("true") != -1:
            print("recibiste un true")
            try:
                if json_memoria != "":
                    lista_1.insertar(json_memoria)
                    print("nodo insertado a la lista")
            except Exception:
                print("no se pudo insertar")
        elif cadena1.find("false") != -1:
            json_memoria = ""
            print("recibiste un false")
        elif cadena1.find("INDEX") != -1:
            try:
                json1 = cadena.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
                json_memoria = json1
                json_analizar = json.loads(json1)
                try:
                    index_ = str(json_analizar["INDEX"])
                    timestamp_ = str(json_analizar["TIMESTAMP"])
                    class_ = str(json_analizar["CLASS"])
                    data_ = str(json_analizar["DATA"]).replace('\'','\"').replace(' ','').replace("None","null")
                    previous_ = str(json_analizar["PREVIOUSHASH"])
                    hash_prueba = SHA_256(index_,timestamp_,class_,data_,previous_)
                    hash_analizar = str(json_analizar["HASH"])
                    if hash_prueba == hash_analizar:
                        server.sendall("true".encode('utf-8'))
                        print("mande verdadero: ")
                    else:
                        server.sendall("false".encode('utf-8'))
                        print("mande falso:")
                except Exception:
                    print("error segundo try")
            except Exception:
                print("Error primer try")
        else:
            print(cadena)

def seleccionar_bloques():
    global json_arbol
    pos = 1
    aux = lista_1.menu_bloques(1)
    print(aux)
    while True:
        key = msvcrt.kbhit()
        if key:
            key1 = ord(msvcrt.getch())
            if key1 == ord('d'):
                if pos > lista_1.tam:
                    pos = lista_1.tam
                else:
                    pos += 1
                os.system('cls')
                aux = lista_1.menu_bloques(pos)
                print(aux)
            elif key1 == ord('a'):
                if pos < 1:
                    pos = 1
                else:
                    pos -= 1
                os.system('cls')
                aux = lista_1.menu_bloques(pos)
                print(aux)
            elif key1 == ord('w'):
                break           


def SHA_256(index1, timestamp1, class1, data1, previousH):
    bloque_analizado = str(index1).encode('utf-8') + str(timestamp1).encode('utf-8') + str(class1).encode('utf-8') + str(data1).encode('utf-8') + str(previousH).encode('utf-8')
    sha = hashlib.sha256(bloque_analizado).hexdigest()
    return str(sha)

hilo2 = threading.Thread(target=menu)
hilo1 = threading.Thread(target=servidor)
hilo1.start()
hilo2.start()