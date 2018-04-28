from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

import math

political_parties_list=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
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
	
	class_type = 1 #Type of the class of the attribute to be analized
	class_list = calc_class_data(class_type, sample_data) #List of the classes
	probabilistic_class_list = [] #List of the probabilities of the every class
	entropy = 0.0

	#Calculate the probability of the every class type to be in the sample data
	for i in range(len(class_list)):
		probabilistic_class_list.append(probability_in_list(class_list[i], sample_data, class_type))
		print("Class " + class_list[i] + ": " + str(probabilistic_class_list[i]))


	base = 2.0
	for i in range(len(class_list)):
		entropy = entropy - (probabilistic_class_list[i] * (math.log(base,probabilistic_class_list[i])))

	print("Entropy of the class: " + str(class_type) + "= " + str(entropy))


	return entropy

#Calculate the probablistic to be found in a list
def probability_in_list(element, list, position):

	data_count = len(list)
	probabability = found_count_in_list(element, list, position) / data_count

	return probabability

#Calculate the count of the elements in a list
def found_count_in_list(element, list, position):

	count = 0
	for i in range(len(list)):
		if (element == list[i][position]):
			count = count + 1
	return count


#Calc the class of an object
def calc_class_data(position, data_list):
	

	#Insert kind of attributes inside the list_attributes
	class_data_list = []

	for i in range(len(data_list)):
		found = False
		for j in range(len(class_data_list)):
			if (class_data_list[j] == data_list[i][position]):
				found = True

		if found == False:
			class_data_list.append(data_list[i][position])

	printList(class_data_list)
	return class_data_list


#Print a list
def printList(list):

	#Printing the list 
	for i in range(len(list)):
		print(list[i])

	return 0



print("Iniciando el programa...")
sample_data_size = 5
sample_data = generar_muestra_pais(sample_data_size)
#x = DecisionTree()
calc_entropy()