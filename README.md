## Practica 2
## Estructura de datos

Creador: *Cristian Suy*<br>
Carnet: 201700918<br>
Universidad de San Carlos de Guatemala<br>

#### Descripcion
En la siguiente practica se realizara un pseudo-Blockchain, debido a que esta practica solo se contara con varios usuarios y un solo servidor, a comparacion de un BlockChain donde cualquier usuario puede ser un servidor-cliente. Se trabajara con un archivo inicial con extension .csv en el cual se encontrara una estructura de formato .json, en la practica cada usuario cargara esos datos y lo enviara al servidor como un bloque, y este servidor se encargara de mandar a los demas usuarios los datos del csv como un archivo .json, cuando estos archivos se mande se creara un Hash, con el cual se corroborara que los datos que se mandaron son correctos y no haya ningun cambio en la transaccion de los datos. Este archivo .json tendra un estructura con la cual se creara un arbol binario, y aplicando los algoritmos necesarios se equilibrara el arbol binario si es necesario creando un arbol binario de busqueda AVL.

#### NOTAS:
Practica realizado en el lenguaje Python, reportes generados con Graphviz y Json.
Estructuras a utilizar e implementar, arbol binario de busqueda AVL, listas dinamicas.