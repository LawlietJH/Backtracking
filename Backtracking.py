
# Algoritmo de Backtracking. Solucion de Laberintos.
# Python 3.6
# By: LawlietJH
# Version: 1.0.0

import time, os
from colorama import Fore, Back, Style, init

init()

class Arbol:
	
	# la variable coordenada es obligatoria, pero si la variable padre no se manda a la funcion, por defecto toma el valor None y tambien en contador, tomara el valor 1 si no se manda nada.
	def __init__(self, coordenada, padre=None, cont=1):		# Constructor de la clase.
		
		self.coord = coordenada		# Posición Del Nodo.
		self.hijos = []				# Conexión a los Hijos.
		self.padre = padre			# Aqui se almacena la coordenada del Nodo Padre
		self.esini = False
		self.esfin = False
		self.cont  = [cont]
	
	def agregar(self, coord, padre):	# Agrega un Nodo a la lista de hijos.
		
		global cont			# La variable global cont sera modificada asi que se declara de esta forma para indicar que modifique la variable global.
		
		cont += 1			# Se aumenta en uno el contador de pasos del algoritmo backtracking.
		
		if not self.buscar(self, coord):					# Si no se encontro la coordenada en el arbol, significa que no esta repetido.
			self.hijos.append(Arbol(coord, padre, cont))	# Agrega un nuevo objeto Arbol con las coordenadas, en la lista de hijos del Nodo Actual.
			return True										# Devuelve True si la coordenada no existe en el arbol y se agrego donde corresponde.
		else:
			return False									# Devuelve False si la coordenada ya existe en el arbol.
	
	def buscar(self, arbol, coord):		# Busca un elemento en el arbol, solo con las coordenadas en [Y, X]
		
		if coord == arbol.coord: return True				# Devuelve True Si encuentra el elemento.
		
		for subarbol in arbol.hijos:						# Recorre el arbol de forma recursiva.
			
			if self.buscar(subarbol, coord): return True	# devuelve True si se encontro el elemento en lo recursivo.
			
		return False										# Devuelve False si aun no lo encuentra.
	
	def profundidad(self, arbol, cont=1):	# Hace un recorrido de profundidad en el arbol.
		
		Y, X = arbol.coord
		if lab[Y][X] == 'F':
			arbol.esfin = True
		
		print(arbol.coord, 'Step:', arbol.cont, 'Ini' if arbol.esini else ('Fin' if arbol.esfin else ''))
		
		for hijo in arbol.hijos:		# Extrae sus hijos y los recorre de forma recursiva.
			
			self.tabs(cont)
			self.profundidad(hijo, cont+1)
	
	def tabs(self, Cont):		# Sirve para mostrar el recorrido en profundidad de forma medio ordenada xD de hasta 32 niveles.
		
		if Cont ==  1: print('\t', end='')
		if Cont ==  2: print('\t| |' + '\t', end='')
		if Cont ==  3: print('\t| |' *  2 + '\t', end='')
		if Cont ==  4: print('\t| |' *  3 + '\t', end='')
		if Cont ==  5: print('\t| |' *  4 + '\t', end='')
		if Cont ==  6: print('\t| |' *  5 + '\t', end='')
		if Cont ==  7: print('\t| |' *  6 + '\t', end='')
		if Cont ==  8: print('\t| |' *  7 + '\t', end='')
		if Cont ==  9: print('\t| |' *  8 + '\t', end='')
		if Cont == 10: print('\t| |' *  9 + '\t', end='')
		if Cont == 11: print('\t| |' * 10 + '\t', end='')
		if Cont == 12: print('\t| |' * 11 + '\t', end='')
		if Cont == 13: print('\t| |' * 12 + '\t', end='')
		if Cont == 14: print('\t| |' * 13 + '\t', end='')
		if Cont == 15: print('\t| |' * 14 + '\t', end='')
		if Cont == 16: print('\t| |' * 15 + '\t', end='')
		if Cont == 17: print('\t| |' * 16 + '\t', end='')
		if Cont == 18: print('\t| |' * 17 + '\t', end='')
		if Cont == 19: print('\t| |' * 18 + '\t', end='')
		if Cont == 20: print('\t| |' * 19 + '\t', end='')
		if Cont == 21: print('\t| |' * 20 + '\t', end='')
		if Cont == 22: print('\t| |' * 21 + '\t', end='')
		if Cont == 23: print('\t| |' * 22 + '\t', end='')
		if Cont == 24: print('\t| |' * 23 + '\t', end='')
		if Cont == 25: print('\t| |' * 24 + '\t', end='')
		if Cont == 26: print('\t| |' * 25 + '\t', end='')
		if Cont == 27: print('\t| |' * 26 + '\t', end='')
		if Cont == 28: print('\t| |' * 27 + '\t', end='')
		if Cont == 29: print('\t| |' * 28 + '\t', end='')
		if Cont == 30: print('\t| |' * 29 + '\t', end='')
		if Cont == 31: print('\t| |' * 30 + '\t', end='')
		if Cont == 32: print('\t| |' * 31 + '\t', end='')


#=======================================================================
#=======================================================================
#=======================================================================


def imprimirLaberinto(lab):
	
	os.system('cls')				# Limpia pantalla.
	
	# Imprimimos el recorrido en el laberinto:
	for y, fila in enumerate(lab):
		
		print(end=Style.BRIGHT+Fore.BLACK+'\n  ')
		
		for x, col in enumerate(fila):
			
			pos = lab[y][x]
			
			if pos == 'I':
				char = Back.CYAN+Fore.CYAN+' I '+Fore.BLACK+Back.RESET				# Se imprime la I con colores.
			elif [y, x] in pila and not [y, x] == fin:								# Si la posicion actual esta en la pila y no es la coordenada final,
				char = Fore.CYAN+'███'+Fore.BLACK									# se imprime para marcar el recorrido de backtracking.
			else:
				if pos == '0': char = '▓▓▓'											# Se imprime en el lugar de los 0's para simular paredes.
				elif pos == 'F':													# Si la coordenada tiene una F
					if pila[-1] == fin:												# Y el ultimo elemento en la pila es igual a la coordenada final, o sea, se encontro el final con backtracking
						char = Back.GREEN+Fore.GREEN+' F '+Fore.BLACK+Back.RESET	# Lo pinta de colores verdes todo el cuadro.
					else:															# Sino se ha encontrado el final, solo pinta la letra verde
						char = Fore.GREEN+' F '+Fore.BLACK
				else: char = '   '													# Sino es nada anterior, solo se imprimen espacios, en las posiciones de los 1's.
			
			# Se imprime el caracter con las especificaciones anteriores, en base a la coordenada en [y, x].
			print(char, end='')
	
	print()					# Imprime en pantalla solo un salto de linea.
	time.sleep(tiempo)		# Hace una pausa del tiempo indicado en la variable global tiempo.
	# Si la variable global solo se usa para leectura, no es necesario indicarla como global y solo se manda a llamar como en el caso anterior.
	

def backtracking(arbol):
	
	global cont, pila		# Las variables globales que se vayan a modificar deben indicarse asi
	
	esnodofinal = True
	finalizado = False
	
	padre = arbol.coord			# Extraemos las coordenadas en Y y X.
	Y, X = padre
	
	if not padre in pila:		# Si no esta la coordenada del elemento padre del arbol actual en la pila, se agrega.
		pila.append(padre)
	else:
		return False			# Si ya esta en la pila, entonces se retorna para no continuar por un camino repetido.
		
	try: 	izq = [lab[Y][X-1], [Y, X-1]]		# Si se sale de la matriz (o sea que ocurre un error, se desborda de la matriz), se va al except.
	except: izq = None
	try: 	arr = [lab[Y-1][X], [Y-1, X]]
	except: arr = None
	try: 	der = [lab[Y][X+1], [Y, X+1]]
	except: der = None
	try: 	aba = [lab[Y+1][X], [Y+1, X]]
	except: aba = None
	
	orden = [aba, der, arr, izq]				# Cambiar al gusto el orden de expansion de nodos aquí.
	
	# Imprimimos el laberinto mientras el algoritmo avance.
	imprimirLaberinto(lab)						# Imprime el laberinto con los pasos actuales que se encuentran en la pila.
	
	
	if orden[0][0] in ['1', 'F'] and not orden[0][1] == arbol.padre:
		esnodofinal = False
		coord = orden[0][1]									# Coordenadas del nodo Hijo.
		if arbol.agregar(coord, padre):						# Agrega en el padre indicado en el alrbol a un hijo con las coordenadas indicadas.
			if orden[0][0] == 'F':
				pila.append(coord)							# Si se encontro el nodo final, se agrega la cordenada a la Pila para mostrar el recorrido mas corto del inicio al final.
				return True									# Si Encontro una F en el laberinto, entonces se retorna para terminar la ejecución.
			finalizado = backtracking(arbol.hijos[-1])		# Si Encontro una F en el laberinto, entonces se retorno para terminar la ejecución y llega por aquí.
			if finalizado: return True						# Se sigue retornando hasta salir de la recursividad y salir completamente de la funcion.
	if orden[1][0] in ['1', 'F'] and not orden[1][1] == arbol.padre:
		esnodofinal = False
		coord = orden[1][1]									# Coordenadas del nodo Hijo.
		if arbol.agregar(coord, padre):						# Agrega en el padre indicado en el alrbol a un hijo con las coordenadas indicadas. 
			if orden[1][0] == 'F':
				pila.append(coord)							# Si se encontro el nodo final, se agrega la cordenada a la Pila para mostrar el recorrido mas corto del inicio al final.
				return True									# Si Encontro una F en el laberinto, entonces se retorna para terminar la ejecución.
			finalizado = backtracking(arbol.hijos[-1])		# Si Encontro una F en el laberinto, entonces se retorno para terminar la ejecución y llega por aquí.
			if finalizado: return True						# Se sigue retornando hasta salir de la recursividad y salir completamente de la funcion.
	if orden[2][0] in ['1', 'F'] and not orden[2][1] == arbol.padre:
		esnodofinal = False
		coord = orden[2][1]									# Coordenadas del nodo Hijo.
		if arbol.agregar(coord, padre):						# Agrega en el padre indicado en el alrbol a un hijo con las coordenadas indicadas. 
			if orden[2][0] == 'F':
				pila.append(coord)							# Si se encontro el nodo final, se agrega la cordenada a la Pila para mostrar el recorrido mas corto del inicio al final.
				return True									# Si Encontro una F en el laberinto, entonces se retorna para terminar la ejecución.
			finalizado = backtracking(arbol.hijos[-1])		# Si Encontro una F en el laberinto, entonces se retorno para terminar la ejecución y llega por aquí.
			if finalizado: return True						# Se sigue retornando hasta salir de la recursividad y salir completamente de la funcion.
	if orden[3][0] in ['1', 'F'] and not orden[3][1] == arbol.padre:
		esnodofinal = False
		coord = orden[3][1]									# Coordenadas del nodo Hijo.
		if arbol.agregar(coord, padre):						# Agrega en el padre indicado en el alrbol a un hijo con las coordenadas indicadas. 
			if orden[3][0] == 'F':
				pila.append(coord)							# Si se encontro el nodo final, se agrega la cordenada a la Pila para mostrar el recorrido mas corto del inicio al final.
				return True									# Si Encontro una F en el laberinto, entonces se retorna para terminar la ejecución.
			finalizado = backtracking(arbol.hijos[-1])		# Si Encontro una F en el laberinto, entonces se retorno para terminar la ejecución y llega por aquí.
			if finalizado: return True						# Se sigue retornando hasta salir de la recursividad y salir completamente de la funcion.
	
	# Si el nodo padre no es nodo final, se le agrega el contador a la lista, 
	# y si entro aqui tambien significa que se esta retrocediendo porque se 
	# llego a un limite y se deben contar los pasos en todo momento.
	if not esnodofinal:
		cont += 1
		arbol.cont.append(cont)
	
	pila.pop()
	
	# Imprimimos de nuevo el laberinto mientras el algoritmo retrocede.
	imprimirLaberinto(lab)
	
	
	


#=======================================================================
#=======================================================================
#=======================================================================



# Variables Globales:
tamX = None		# dimensiones del laberinto
tamY = None
pila = []		# pila para el recorrido del algoritmo backtracking.
lab = []		# para almacenar el laberinto.
ini = []		# Para la Coordenada Inicial.
fin = []		# Para la Coordenada Final.
cont = 1		# Contador de Pasos.
tiempo = 0.02	#Tiempo de segundos por frame.


# Se carga el laberinto desde el archivo en modo lectura (r de read) y se almacena en la variable f, f solo funcionará dentro del bloque WITH.
with open('laberinto_01.txt','r') as f:
	
	lab = f.read()				# Leemos el contenido de el archivo y se extrae como una sola cadena.
	lab = lab.split('\n')		# Generamos una lista con la cadena dividida en saltos de linea, o sea, se genera la lista con las filas completas.
	
	tamY = len(lab)				# Extraemos las dimensiones en Y, que es la cantidad de Filas.
	tamX = len(lab[0])			# Extraemos las dimensiones en X, que es la cantidad de elementos en una fila, o sea, las columnas.
	
	# Buscamos las coordenadas Inicial y Final.
	for y, fila in enumerate(lab):				# extraemos una fila en cada iteracion y contamos con enumerate() en y, desde la posicion 0, en cada iteracion y aumenta 1.
		for x, campo in enumerate(fila):		# extraemos una columna en cada iteracion y contamos con enumerate() en x, desde la posicion 0, en cada iteracion x aumenta 1 
			if   campo == 'I': ini = [y, x]		# Agregamos la coordenada Inicial si se encontro.
			elif campo == 'F': fin = [y, x]		# Agregamos la coordenada Final si se encontro.
	
	# Cerramos el archivo almacenado en la variable f.
	f.close()



# Genera el objeto tree de la clase Arbol:
tree = Arbol(ini)		# Le pasamos la posicion inicial como raiz del arbol.
tree.esini = True		# Indicamos que esta posicion es la Inicial.
backtracking(tree)		# Iniciamos el recorrido del laberinto.
imprimirLaberinto(lab)	# Imprimimos una ultima vez el laberinto ya con todo el recorrido despues de hacer backtracking.

# Imprimimos la pila con el recorrido del algoritmo:
print(Fore.GREEN+'\n\n Recorrido Final por Coordenadas:', pila)

# Recorrido en Profundidad:
# ~ print(Fore.GREEN+'\n\n Recorrido en Profundidad:\n')
# ~ tree.profundidad(tree)










