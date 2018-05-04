#from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

import math

political_parties_list=["ACCESIBILIDAD SIN EXCLUSION", "ACCION CIUDADANA", "ALIANZA DEMOCRATA CRISTIANA", 
"DE LOS TRABAJADORES", "FRENTE AMPLIO	INTEGRACION NACIONAL", "LIBERACION NACIONAL", "MOVIMIENTO LIBERTARIO", 
"NUEVA GENERACION", "RENOVACION COSTARRICENSE", "REPUBLICANO SOCIAL CRISTIANO", "RESTAURACION NACIONAL", 
"UNIDAD SOCIAL CRISTIANA"]



class Decision_tree_model:

	attrib_value_entropy_general_list = []
	r = ""
	sample_data = None

	def __init__(self, sample_data, r):
		self.r = r
		self.sample_data = sample_data
		self.calc_decision_tree(sample_data, r)
		

	#Calc the order of the attributes for to do the decision tree
	def calc_decision_tree(self, sample_data, r):
		if (self.calc_info_gain(sample_data, r)) == True:
			print("Realización del árbol de decisión con éxito")
		else:
			print("ERROR")
		return 0

	#Calc the entropy of the attributes
	def calc_info_gain(self, sample_data, r):

		#if len(sample_data) == 0:
		#	print("Realización de la ejecución del programa con éxito")
		#else:		
		print("Estos son los datos de muestra")
		print("")
		print(sample_data)
		print("")

		attributes_count = 0
		class_list = []
		class_type = 0
		self.attrib_value_entropy_general_list = []


		if r == "r1":
			attributes_count = len(sample_data[0]) - 2
			class_type = len(sample_data[0]) - 2
			class_list = self.calc_class_data(class_type,sample_data)
		elif r == "r2":
			attributes_count = len(sample_data[0]) - 2
			class_type = len(sample_data[0]) - 1
			class_list = self.calc_class_data(class_type,sample_data)
		else:
			attributes_count = len(sample_data[0]) - 1
			class_type = len(sample_data[0]) - 1
			class_list = self.calc_class_data(class_type,sample_data)
		
		print("_Impresión 1")
		
		information_gain_list =[]
		print("__Impresion 2")
		class_entropy_num = self.class_entropy(class_type, sample_data)
		position = 0
		attributes_max = 0 
		index = 0

		for i in range(attributes_count): #Travel the list of attributes
			factor = 0
			#print("___Impresión 3")
			attrib_value_list = self.calc_class_data(i, sample_data)
			attrib_value_entropy_list = [] #Store the entropy of the values of an attribute of the data
			for j in range(len(attrib_value_list)): #Travel the list of the values of the attributes
				#print("____Impresión 4")
				attrib_value_entropy_list.append(self.calc_attrib_value_entropy(j,attrib_value_list[j],sample_data,class_list, class_type, i))
			for k in range(len(attrib_value_entropy_list)):
				#print("____Impresion 5")
				factor = factor + ((self.calc_attrib_value_found(attrib_value_list[k],sample_data,i)/len(sample_data)) * attrib_value_entropy_list[k])
			entropy_attribute_rest = class_entropy_num - factor
			information_gain_list.append(entropy_attribute_rest)
		attributes_max = max(information_gain_list)
		index = information_gain_list.index(attributes_max)
		print ("Lista con todas las entropías de los valores de los atributos " , self.attrib_value_entropy_general_list)
		print("Indice del attributo con mayor ganancia :", index)
		print("Information gain of the attributes " + str(information_gain_list))
		
		print("Lista con los valores que poseen entropía igual cero y sus respectivas clases" , self.calc_attrib_value_class(index))
		print("Lista con los valores que poseen entropía diferente a cero y sus respectivas clases", self.calc_no_attrib_value_class(index))


	def calc_attrib_value_class(self, index):
		val = self.attrib_value_entropy_general_list[index] #list of the values with a class
		n = len(val)
		i = 0
		result_list = []
		while (i<n):
			if (val[i][1] == 0):
				tmp = val[i][0]
				for x in self.sample_data:
					if (tmp == x[index]):
						if (self.r == "r1"):
							result_list.append([tmp, x[len(x) - 2]])
						else:
							result_list.append([tmp, x[len(x) - 1]])
						break
			i += 1
		return result_list

	def calc_no_attrib_value_class(self, index):
		val = self.attrib_value_entropy_general_list[index] #list of the values with a class
		n = len(val)
		i = 0
		result_list = []
		while (i<n):
			if (val[i][1] != 0):
				result_list.append(val[i][0])
			i += 1
		return result_list

	#Calculate the count of a value of a attribute according to a class in a data
	def found_count_in_list(self, class_element,attrib_value,sample_data, class_list,class_type, attrib_value_position):
		count = 0
		class_positions_list = []
		attrib_value_positions_list = []
		for i in range(len(sample_data)):
			#print("")
			#print("Imprimiendo la clase de elemento" + str(class_element))
			#print("IMP el dato en la posición " + str(class_type)+" de la lista")
			if sample_data[i][class_type] == class_element:
				class_positions_list.append(i)
				#print("")
				#print("Añadiendo el elemento " + str(i) + " a la lista de posiciones de clase")
		for j in range(len(sample_data)):
			#print("")
			#print("Imprimiendo el valor del atributo " + str(attrib_value))
			#print("IMP el dato en la posición " + str(attrib_value_position) + " de atributos de la lista")
			if sample_data[j][attrib_value_position] == attrib_value:
				attrib_value_positions_list.append(j)
				#print("")
				#print("Añadiendo el elemento " + str(j) + " a la lista de posiciones de valores de atributos")
		for k in range(len(class_positions_list)):
			for l in range(len(attrib_value_positions_list)):
				if(class_positions_list[k] == attrib_value_positions_list[l]):
					count = count + 1
		#print("Cuenta de un attributo: " + str(count))
		return count

	#Calculate the count in which a value of an attribute is found
	def calc_attrib_value_found(self, attrib_value,sample_data,attribute_position):
		count = 0
		for i in range(len(sample_data)):
			if sample_data[i][attribute_position] == attrib_value:
				count = count + 1
		print("Cuenta del total de veces que aparece el valor del atributo " + str(count))
		return count

	#Calculate the probability of a value inside an attribute of the data
	def calc_value_prob(self, class_element,attrib_value,sample_data,class_list,class_type,attrib_value_position):
		prob_value = self.found_count_in_list(class_element,attrib_value,sample_data, class_list, class_type,attrib_value_position)/self.calc_attrib_value_found(attrib_value,sample_data,attrib_value_position)
		print("Prob_value " + str(prob_value))
		return prob_value

	#Calulate the entropy of a value of an attribute of the data
	def calc_attrib_value_entropy(self, attribute_value_list, attrib_value,sample_data, class_list, class_type, attrib_value_position):
		value_prob_list = [] #List of the probabilities of the every class
		entropy = 0.0

		for i in range(len(class_list)): #class list of the round
			#append the prob of one value according to a class
			value_prob_list.append(self.calc_value_prob(class_list[i],attrib_value, sample_data, class_list,class_type,attrib_value_position))
		base = 2.0
		for j in range(len(value_prob_list)):
			print ("IMPRIMIENDO EL RESULTADO DE LA PROBABILIDAD DE UN VALOR DE UN ATRIBUTO " + str(value_prob_list[j]))
			if (value_prob_list[j] == 0):
				entropy = entropy + 0
			else:
				entropy = entropy - (value_prob_list[j] * math.log(value_prob_list[j], base))		
		print("Imprimiendo la entropía del valor " , attrib_value, entropy)
		print("Imprimiendo la posicion del valor del atributo ", attrib_value_position)

		if len(self.attrib_value_entropy_general_list) == attrib_value_position:
			self.attrib_value_entropy_general_list.append([])
		self.attrib_value_entropy_general_list[attrib_value_position].append([attrib_value, entropy])
		return entropy

	#Calculate the probablistic to be found in a list
	def probability_in_list(self, element, list, position):
		data_count = len(list)
		probabability = self.count_element(element, list, position) / data_count
		return probabability

	def count_element(self, element, sample_data, class_type):
		count = 0
		for i in range(len(sample_data)):
			if element == sample_data[i][class_type]:
				count = count + 1
		return count

	#Calculate the probablistic to be found in a class
	def class_entropy(self, class_type, sample_data):
		probabilistic_class_list = [] #List of the probabilities of the every class
		class_list = self.calc_class_data(class_type, sample_data)
		entropy = 0.0
		for i in range(len(class_list)):
			probabilistic_class_list.append(self.probability_in_list(class_list[i], sample_data, class_type))
			#print("Class " + class_list[i] + ": " + str(probabilistic_class_list[i]))
		base = 2.0
		for i in range(len(class_list)):
			if (probabilistic_class_list[i] == 0):
				entropy = entropy + 0
			else:
				entropy = entropy - (probabilistic_class_list[i] * (math.log(probabilistic_class_list[i],base)))
		#print("Entropy of the class: " + str(i) + "= " + str(entropy))
		return entropy

	#Calc the class of an object
	def calc_class_data(self, position, data_list):
		class_data_list = []
		for i in range(len(data_list)):
			found = False
			for j in range(len(class_data_list)):
				if (class_data_list[j] == data_list[i][position]):
					found = True
			if found == False:
				class_data_list.append(data_list[i][position])
		#print("Impresión de la lista de clase de los datos" + str(class_data_list))
		return class_data_list


class Decision_tree:

	element = None
	children = None
	decisions = None

	def __init__(self, element):
		self.element = element #Index of the attribute in the data
		self.children = []
		self.decisions = []

	def add_element(self, decision_tree, element, super_element):
		sub_decision_tree = search_sub_decision_tree(decision_tree, super_element)
		sub_decision_tree.children.append(Decision_tree(element))

	def search_sub_decision_tree(self, decision_tree, element):
		if decision_tree.element == element:
			return decision_tree
		for sub_decision_tree  in decision_tree.children:
			searched_sub_decision_tree = search_sub_decision_tree(sub_decision_tree, element)
			if (searched_sub_decision_tree != None):
				return searched_sub_decision_tree
		return None
		










print("Iniciando el programa...")
sample_data = [['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 55, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'],['HEREDIA', 'FLORES', 20037, 6.96, 2878.88, 'Urbana', 'Hombre', 41, 5763, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.61, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'],['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 48, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA']]
objeto = Decision_tree_model(sample_data, "r2")