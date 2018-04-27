from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

list_political_parties=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
"DE LOS TRABAJADORES", "FRENTE AMPLIO	INTEGRACION NACIONAL", "LIBERACION NACIONAL", "MOVIMIENTO LIBERTARIO", 
"NUEVA GENERACION", "RENOVACION COSTARRICENSE", "REPUBLICANO SOCIAL CRISTIANO", "RESTAURACION NACIONAL", 
"UNIDAD SOCIAL CRISTIANA"]


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


		return list_attributes

	##calc the class of an object 
	def calc_class_data(position, dataList):
		"""Insert kind of attributes inside the list_attributes"""
		classDataList = []
		for i in range(len(dataList)):
			found = False
			for j in range(len(classDataList)):
				if (classDataList[j] == dataList[i][position])
					found = True

			if found == False:
				classDataList.append(dataList[i][position])

		return classDataList

	def printList(list):

		"""Printing the list of the attributes"""
		for i in range(len(list)):
			print(list[i])

		return 0



print("Iniciando el programa...")
data = generar_muestra_pais(5)
x = DecisionTree()
x.calc_entropy()