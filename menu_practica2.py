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
        print("----------Practica 2---------")
        print("1.Insertar Bloque")
        print("2.Seleccionar Bloque")
        print("3.Reportes")
        print("4.Cerrar Programa")
        opcion = int(input("Que opcion desea realizar... "))
        if opcion == 1:
            archivo_entrada = str(input("Ingrese el nombre del archivo con extension .csv...   "))
            insertarBloque(archivo_entrada,server)
            print("area de insertar bloques")
        elif opcion == 2:
            print("Este apartado es para seleccionar bloques")
        elif opcion == 3:
            print("area para realizar reportes")
        elif opcion == 4:
            print("Gracias :v")
            break

def insertarBloque(archivo, servidor1):
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
    previous_ = str(dd["PREVIOUSHASH"])
    hash_prueba = SHA_256(index_,timestamp_,class_,data_,previous_)
    temporal = {"HASH": hash_prueba}
    archivo_json.update(temporal)
    json_final = json.dumps(archivo_json).replace("\\n",'').replace("\\",'')
    server.sendall(str(json_final).encode('utf-8'))

def analisis_json(cadena):
        cadena1 = str(cadena)
        if cadena1.find("true") != -1:
            print("recibiste un true")
        elif cadena1.find("false") != -1:
            print("recibiste un false")
        elif cadena1.find("INDEX") != -1:
            try:
                json1 = cadena.replace(chr(34)+chr(123),chr(123)).replace(chr(125)+chr(34),chr(125))
                json_analizar = json.loads(json1)
                #verdadero = 'true'
                #falso = 'false'
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


def SHA_256(index1, timestamp1, class1, data1, previousH):
    bloque_analizado = str(index1).encode('utf-8') + str(timestamp1).encode('utf-8') + str(class1).encode('utf-8') + str(data1).encode('utf-8') + str(previousH).encode('utf-8')
    sha = hashlib.sha256(bloque_analizado).hexdigest()
    return str(sha)

hilo2 = threading.Thread(target=menu)
hilo1 = threading.Thread(target=servidor)
hilo1.start()
hilo2.start()