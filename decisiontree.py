from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

list_political_parties=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
"DE LOS TRABAJADORES", "FRENTE AMPLIO	INTEGRACION NACIONAL", "LIBERACION NACIONAL", "MOVIMIENTO LIBERTARIO", 
"NUEVA GENERACION", "RENOVACION COSTARRICENSE", "REPUBLICANO SOCIAL CRISTIANO", "RESTAURACION NACIONAL", 
"UNIDAD SOCIAL CRISTIANA"]


##Creación de la clase árbol de decisión
"""class DecisionTree:
	

	#Initilization of the tree
	def __init__(self):
		self.nodes = []

	## Creation of the class node for the decision tree
	class Node:
		
		#Initilization of the class
		def __init__(self, attribute):
			self.attribute = attribute
			self.value = ""
	"""

##Calc the entropy of the attributes
def calc_entropy():
	
	attributes_list = calc_class_data(0, data)
	probalistic_class_data = []

	for i in range(len(attributes_list)):
		probalistic_class_data.append(probability_in_list(attributes_list[i], attributes_list))



	return list_attributes

#Calculate the probablistic to be found in a list
def probability_in_list(element, list):

	data_count = len(list)
	probabability = found_count_in_list(element, list) / data_count

	return probabability

#Calculate the count of the elements in a list
def found_count_in_list(element, list):

	count = 0
	for i in range(len(list)):
		if (element == list[i]):
			count = count + 1
	return count


#Calc the class of an object
def calc_class_data(position, dataList):
	

	#Insert kind of attributes inside the list_attributes
	classDataList = []
	class_data_found_coun = []

	for i in range(len(dataList)):
		found = False
		for j in range(len(classDataList)):
			if (classDataList[j] == dataList[i][position]):
				found = True

		if found == False:
			classDataList.append(dataList[i][position])

	printList(classDataList)
	return classDataList


	#def calc_prob_class_data():

#Print a list
def printList(list):

	#Printing the list 
	for i in range(len(list)):
		print(list[i])

	return 0



print("Iniciando el programa...")
data_sample_size = 5
sample_data = generar_muestra_pais(data_sample_size)
#x = DecisionTree()
calc_class_data(1,data)