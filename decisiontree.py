from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

import math

political_parties_list=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
"DE LOS TRABAJADORES", "FRENTE AMPLIO	INTEGRACION NACIONAL", "LIBERACION NACIONAL", "MOVIMIENTO LIBERTARIO", 
"NUEVA GENERACION", "RENOVACION COSTARRICENSE", "REPUBLICANO SOCIAL CRISTIANO", "RESTAURACION NACIONAL", 
"UNIDAD SOCIAL CRISTIANA"]

#Calc the order of the attributes for to do the decision tree
def calc_decision_tree(sample_data):
	if (calc_info_gain(sample_data, 22)) == True:
		print("Realización del árbol de decisión con éxito")
	else:
		print("ERROR")
	return 0

#Calc the entropy of the attributes
def calc_info_gain(sample_data, round_number):

	#if len(sample_data) == 0:
	#	print("Realización de la ejecución del programa con éxito")
	#else:		
	print("Estos son los datos de muestra")
	print("")
	print(sample_data)
	print("")
	
	print("_Impresión 1")
	class_list = calc_class_data(round_number,sample_data)
	information_gain_list =[]
	print("__Impresion 2")
	class_entropy_num = class_entropy(round_number, sample_data)
	position = 0
	attributes_count = len(sample_data[0]) - 2
	for i in range(attributes_count): #Travel the list of attributes
		print("___Impresión 3")
		attrib_value_list = calc_class_data(i, sample_data)
		attrib_value_entropy_list = []
		for j in range(len(attrib_value_list)):
			attrib_value_entropy_list.append(calc_attrib_value_entropy(j,attribute_value_list[j],sample_data,round_number))

			attrib_value_entropy_list = calc_attrib_value_entropy(calc)

		for j in range(len(attrib_value_list)):
			print("____Impresion 4")
			attrib_value_entropy_list.append(calc_attrib_value_entropy(j, attrib_value_list[j],sample_data,
				class_list, round_number))
		"""for k in range(len(attrib_value_entropy_list)):
			print("_____Impresion 5")
			factor = factor + (calc_class_data(i, attrib_value_list[j]) * attrib_value_entropy_list[k])
		info_gain = info_gain - factor
		information_gain_list.append(info_gain)
	for l in range(len(information_gain_list)):
		major_element = information_gain_list[l]
		if (information_gain_list[l]) >= major_element:
			major_element = information_gain_list[l]
			position = l
	#	return calc_info_gain(sample_data[position].pop(l),round_number)
	"""

#Calculate the count of the elements in a list
def found_count_in_list(class_element, sample_data, position):


	count = 0
	for i in range(len(sample_data)):
		if (class_element == sample_data[i][position]):
			count = count + 1
	return count


def calc_attrib_value_found(class_list,sample_data,round_number):
	count = 0
	for i in range(len(sample_data)):
		if sample_data[i][attribute_value_position] == attrib_value:
			count = count + 1
	return count

def calc_value_prob(class_element,attrib_value,sample_data,class_list,round_number):
	for i in range(len(sample_data)):
		prob_value_list= found_count_in_list(class_element,attrib_value,sample_data,attribute_value_position)/calc_attrib_value_found(attribute_value_position, sample_data,attrib_value)
	return prob_value_list

def calc_attrib_value_entropy(attribute_value_list, attrib_value,sample_data, class_list, round_number):
	value_prob_list = [] #List of the probabilities of the every class
	entropy = 0.0
	for i in range(len(class_list)): #class list of the round
		#append the prob of one value according to a class
		value_prob_list.append(calc_value_prob(class_list[i],attrib_value, sample_data, class_list, round_number)


		for j in range(len(class_list)):
			attrib_value_prob_list.append(calc_attrib_value_prob(attribute_value_position, attrib_value,sample_data, round_number))
		print("Value " + attrib_value + " " + str(attrib_value_prob_list[i]))
	base = 2.0
	for i in range(len(class_list)):
		entropy = entropy - (value_prob_list[i] * (math.log(base,(value_prob_list[i]))))
	print("Entropy of the value " + str(attribute_value) + "= " + str(entropy))


#Calculate the probablistic to be found in a list
def probability_in_list(element, list, position):
	data_count = len(list)
	probabability = found_count_in_list(element, list, position) / data_count

	return probabability

#Calculate the probablistic to be found in a class
def class_entropy(round_number, sample_data):
	probabilistic_class_list = [] #List of the probabilities of the every class
	class_list = calc_class_data(round_number, sample_data)
	entropy = 0.0
	for i in range(len(class_list)):
		probabilistic_class_list.append(probability_in_list(class_list[i], sample_data, round_number))
		print("Class " + class_list[i] + ": " + str(probabilistic_class_list[i]))
	base = 2.0
	for i in range(len(class_list)):
		entropy = entropy - (probabilistic_class_list[i] * (math.log(base,probabilistic_class_list[i])))
	print("Entropy of the class: " + str(i) + "= " + str(entropy))
	return entropy

#Calc the class of an object
def calc_class_data(position, data_list):
	class_data_list = []
	for i in range(len(data_list)):
		found = False
		for j in range(len(class_data_list)):
			if (class_data_list[j] == data_list[i][position]):
				found = True
		if found == False:
			class_data_list.append(data_list[i][position])
	print("Impresión de la lista de clase de los datos" + str(class_data_list))
	return class_data_list


print("Iniciando el programa...")
calc_decision_tree(generar_muestra_pais(5))