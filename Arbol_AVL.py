from nodo import Nodo_AVL
import os

class Nodoavl(object): 
	def __init__(self, valor): 
		self.valor = valor 
		self.izquierdo = None
		self.derecho = None
		self.altura = 1
		self.factor = 0
 
class arbol_AVL(object): 
	def insertar(self, root, key):  
		if not root: 
			return Nodoavl(key) 
		elif key < root.valor: 
			root.izquierdo = self.insertar(root.izquierdo, key) 
		else: 
			root.derecho = self.insertar(root.derecho, key) 

		root.altura = 1 + max(self.Altura(root.izquierdo), 
						self.Altura(root.derecho)) 

		balanceo = self.Factor_Equilibrio(root)
		root.factor = balanceo 
		# Case 1: rotacion simple a la izquierda 
		if balanceo > 1 and key < root.izquierdo.valor: 
			return self.RotacionD(root) 
		# Case 2: rotacion simple a la derecha
		if balanceo < -1 and key > root.derecho.valor: 
			return self.RotacionI(root) 
		# Case 3: rotacion doble por la izquierda 
		if balanceo > 1 and key > root.izquierdo.valor: 
			root.izquierdo = self.RotacionI(root.izquierdo) 
			return self.RotacionD(root) 
		# Case 4: rotacion doble por la derecha 
		if balanceo < -1 and key < root.derecho.valor: 
			root.derecho = self.RotacionD(root.derecho) 
			return self.RotacionI(root) 
		return root 

	def RotacionI(self, raiz): 
		y = raiz.derecho 
		T2 = y.izquierdo 
		y.izquierdo = raiz 
		raiz.derecho = T2 
		raiz.altura = 1 + max(self.Altura(raiz.izquierdo), 
						self.Altura(raiz.derecho)) 
		y.altura = 1 + max(self.Altura(y.izquierdo), 
						self.Altura(y.derecho))
		balanceo1 = self.Factor_Equilibrio(raiz)
		raiz.factor = balanceo1
		balanceo1 = self.Factor_Equilibrio(y)
		y.factor = balanceo1  
		return y 

	def RotacionD(self, raiz): 
		y = raiz.izquierdo 
		T3 = y.derecho 
		y.derecho = raiz 
		raiz.izquierdo = T3 
		raiz.altura = 1 + max(self.Altura(raiz.izquierdo), 
						self.Altura(raiz.derecho)) 
		y.altura = 1 + max(self.Altura(y.izquierdo), 
						self.Altura(y.derecho))
		balanceo1 = self.Factor_Equilibrio(raiz)
		raiz.factor = balanceo1
		balanceo1 = self.Factor_Equilibrio(y)
		y.factor = balanceo1 
		return y 

	def Altura(self, root): 
		if not root: 
			return 0
		return root.altura 

	def Factor_Equilibrio(self, root): 
		if not root: 
			return 0
		return self.Altura(root.izquierdo) - self.Altura(root.derecho) 

	def preOrdenC(self, root): 
		if not root: 
			return
		print("{0} -> ".format(root.valor), end="") 
		self.preOrdenC(root.izquierdo) 
		self.preOrdenC(root.derecho)
	
	def inOrdenC(self, root): 
		if not root: 
			return
		self.inOrdenC(root.izquierdo)
		print("{0} -> ".format(root.valor), end="")  
		self.inOrdenC(root.derecho)
	
	def posOrdenC(self, root): 
		if not root: 
			return
		self.posOrdenC(root.izquierdo)
		self.posOrdenC(root.derecho)
		print("{0} -> ".format(root.valor), end="")  

	def GraficaPre(self,root):
		archivo = "PreOrden.jpg"
		a = open("Arbol2.dot","w")
		a.write("digraph lista{\n")
		a.write("rankdir=LR; \n")
		a.write("node[shape = record];\n")
		a.write(self.preOrdenG(root))
		a.write(" \n}")
		a.close()
		os.system("dot -Tjpg Arbol2.dot -o "+archivo)
		os.system(archivo)

	def Graficar(self,root):
		archivo = "Arbol.jpg"
		a = open("Arbol1.dot","w")
		a.write("digraph lista{\n")
		a.write("node [shape = circle, style=filled, fillcolor=seashell2];\n")
		a.write(self._graficar1(root))
		a.write(" \n}")
		a.close()
		os.system("dot -Tjpg Arbol1.dot -o "+archivo)
		os.system(archivo)

	def _graficar1(self, raiz):
		cuerpo = ""
		if(raiz is not None):
			id1=""+raiz.valor
			id2=id1.split('-')
			cuerpo +="\"Carnet:"
			cuerpo += id2[0]
			cuerpo += "\n Nombre:"
			cuerpo += id2[1]
			cuerpo += "\n Altura:"
			cuerpo += str(raiz.altura-1)
			cuerpo += "\n Factor Equilibrio:"
			cuerpo+= str(raiz.factor)
			cuerpo +="\""
			cuerpo += ";"
			if raiz.izquierdo is not None :
				id1=""+raiz.valor
				id2=id1.split('-')
				cuerpo +="\"Carnet:"
				cuerpo += id2[0]
				cuerpo += "\n Nombre:"
				cuerpo += id2[1]
				cuerpo += "\n Altura:"
				cuerpo += str(raiz.altura-1)
				cuerpo += "\n Factor Equilibrio:"
				cuerpo+= str(raiz.factor)
				cuerpo +="\""
				cuerpo += " -> \n"
				cuerpo += self._graficar1(raiz.izquierdo)
			if raiz.derecho is not None:
				id1=""+raiz.valor
				id2=id1.split('-')
				cuerpo +="\"Carnet:"
				cuerpo += id2[0]
				cuerpo += "\n Nombre:"
				cuerpo += id2[1]
				cuerpo += "\n Altura:"
				cuerpo += str(raiz.altura-1)
				cuerpo += "\n Factor Equilibrio:"
				cuerpo+= str(raiz.factor)
				cuerpo +="\""
				cuerpo += " -> \n"
				cuerpo += self._graficar1(raiz.derecho)
		return cuerpo

	def preOrdenG(self, raiz):
		cuerpo = ""
		if(raiz is not None):
			id1=""+raiz.valor
			id2=id1.split('-')
			cuerpo += "\""
			cuerpo += id2[0]
			cuerpo += "\n"
			cuerpo += id2[1]
			cuerpo +="\""
			if(raiz.izquierdo is not None):
				cuerpo += "->"
				cuerpo += self.preOrdenG(raiz.izquierdo)
			if(raiz.derecho is not None):
				cuerpo += "->"
				cuerpo += self.preOrdenG(raiz.derecho)						
		return cuerpo

	def GraficaIn(self, root):
		archivo = "inOrden.jpg"
		a = open("Arbol3.dot","w")
		a.write("digraph lista{\n")
		a.write("rankdir=LR; \n")
		a.write("node[shape = record];\n")
		a.write(self.inOrdenG(root))
		a.write(" \n}")
		a.close()
		os.system("dot -Tjpg Arbol3.dot -o "+archivo)
		os.system(archivo)
	
	def inOrdenG(self, raiz):
		cuerpo = ""
		if(raiz is not None):
			if(raiz.izquierdo is not None):
				cuerpo += self.inOrdenG(raiz.izquierdo)
				cuerpo += "->"
			id1=""+raiz.valor
			id2=id1.split('-')
			cuerpo += "\""
			cuerpo += id2[0]
			cuerpo += "\n"
			cuerpo += id2[1]
			cuerpo +="\""
			if(raiz.derecho is not None):
				cuerpo += "->"
				cuerpo += self.inOrdenG(raiz.derecho)						
		return cuerpo

	def GraficaPos(self, root):
		archivo = "posOrden.jpg"
		a = open("Arbol4.dot","w")
		a.write("digraph lista{\n")
		a.write("rankdir=LR; \n")
		a.write("node[shape = record];\n")
		a.write(self.posOrdenG(root))
		a.write(" \n}")
		a.close()
		os.system("dot -Tjpg Arbol4.dot -o "+archivo)
		os.system(archivo)
	
	def posOrdenG(self, raiz):
		cuerpo = ""
		if(raiz is not None):
			if(raiz.izquierdo is not None):
				cuerpo += self.posOrdenG(raiz.izquierdo)
				cuerpo += "->"
			if(raiz.derecho is not None):
				cuerpo += self.posOrdenG(raiz.derecho)
				cuerpo += "->"
			id1=""+raiz.valor
			id2=id1.split('-')
			cuerpo += "\""
			cuerpo += id2[0]
			cuerpo += "\n"
			cuerpo += id2[1]
			cuerpo +="\""					
		return cuerpo