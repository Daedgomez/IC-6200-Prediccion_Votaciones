from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

import math

political_parties_list=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
"DE LOS TRABAJADORES", "FRENTE AMPLIO	INTEGRACION NACIONAL", "LIBERACION NACIONAL", "MOVIMIENTO LIBERTARIO", 
"NUEVA GENERACION", "RENOVACION COSTARRICENSE", "REPUBLICANO SOCIAL CRISTIANO", "RESTAURACION NACIONAL", 
"UNIDAD SOCIAL CRISTIANA"]

#Calc the order of the attributes for to do the decision tree
def calc_decision_tree(sample_data):
	if (calc_info_gain(sample_data, [])) == True:
		print("Realización del árbol de decisión con éxito")
	return 0

#Calc the entropy of the attributes
def calc_info_gain(sample_data, result_list):

	#if len(sample_data) == 0:
	#	print("Realización de la ejecución del programa con éxito")
	#else:		
		print("Estos son los datos de muestra")
		print("")
		print(sample_data)
		print("")

		#class_type = 22 #Type of the class of the attribute to be analized
		#class_list = calc_class_data(class_type, sample_data) #List of the classes
		round_number = 22
		class_list = calc_class_data(round_number,sample_data)
		information_gain_list =[]
		class_entropy_num = class_entropy(round_number, sample_data)
		
		for i in range(len(sample_data)-2):
			attrib_value_list = calc_class_data(i, sample_data)
			info_gain = class_entropy(round_number, sample_data)
			attrib_value_entropy_list = calc_attrib_value_entropy(j, attrib_value_list[j],sample_data, class_list, round_number)
			info_gain = class_entropy(round_number, sample_data)
			for j in range(len(attrib_value_list)):
				info_gain = info_gain * (calc_class_data())



def calc_attrib_value_found(attribute_value_position,sample_data,round_number):
	count = 0
	for i in range(sample_data):
		if sample_data[i][attribute_value_position] == sample_data[i][round_number]:
			count = count + 1
	return count

def calc_attrib_value_prob(attribute_value_position,attrib_value,sample_data,round_number,):
	probabability = calc_attrib_value_found(attribute_value_position, sample_data,round_number) / 
					found_count_in_list(attrib_value, sample_data,attribute_value_position)
	return probabability

def calc_attrib_value_entropy(attribute_value_position, attrib_value,sample_data, class_list, round_number):
	attrib_value_prob_list = [] #List of the probabilities of the every class
	for i in range(len(sample_data)):
		for j in range(len(class_list)):
			attrib_value_prob_list.append(calc_attrib_value_prob(attribute_value_position, attrib_value,sample_data, class_list[j], round_number))
		print("Value " + attrib_value + " " + str(attrib_value_prob_list[i])
	base = 2.0
	for i in range(len(class_list)):
		entropy = entropy - (attrib_value_prob_list[i] * (math.log(base,attrib_value_prob_list[i])))
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
	for i in range(len(class_list)):
		probabilistic_class_list.append(probability_in_list(class_list[i], sample_data, round_number))
		print("Class " + class_list[i] + ": " + str(probabilistic_class_list[i]))
	base = 2.0
	for i in range(len(class_list)):
		entropy = entropy - (probabilistic_class_list[i] * (math.log(base,probabilistic_class_list[i])))
	print("Entropy of the class: " + str(class_type) + "= " + str(entropy))

#Calculate the count of the elements in a list
def found_count_in_list(element, list, position):
	count = 0
	for i in range(len(list)):
		if (element == list[i][position]):
			count = count + 1
	return count


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
	print(class_data_list)
	return class_data_list


print("Iniciando el programa...")
calc_decision_tree(generar_muestra_pais(1000))