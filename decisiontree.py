import from.tec.ic.ia.p1.g09 import generar_muestra_pais, generar_muestra_provinca



##Creación de la clase árbol de decisión
class DecisionTree:
	

	"""docstring for DecisionTree"""
	def __init__(self):
		self.nodes = []


## Creación de la clase nodo para el árbol de decisiones
class Node:
	"""docstring for Node"""
	def __init__(self, attribute, value):
		self.attribute = attribute
		self.value = value
		

		
