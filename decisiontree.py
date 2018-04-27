from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia


##Creación de la clase árbol de decisión
class DecisionTree:
	

	"""Initilization of the tree"""
	def __init__(self):
		self.nodes = []


	## Creation of the class node for the decision tree
	class Node:
		
		"""Initilization of the class"""
		def __init__(self, attribute):
			self.attribute = attribute
			self.value = ""

	##Calc the entropy of the attributes
	def calc_entropy():
		list_attributes = []

		"""Insert kind of attributes inside the list_attributes"""
		for i in range(len(data[0])):
			list_attributes.append("attribute"+str(i))


		"""Printing the list of the attributes"""
		for i in range(len(list_attributes)):
			print(list_attributes[i])

		return list_attributes

print("Iniciando el programa...")
data = generar_muestra_pais(5)
x = DecisionTree()
x.calc_entropy()