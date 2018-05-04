from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia
import copy # Para hacer deepcopy de variables
import math


class Decision_tree_model:

	attrib_value_entropy_general_list = []
	r = ""
	dt = None

	def __init__(self, sample_data, r, umbral):
		self.r = r
		self.dt  = self.calc_info_gain(self.convert_to_interval(sample_data), r)
		
		
	def test(self,data):
		data = self.convert_to_interval([data])
		return self.testt(data[0],self.dt)

	def testt(self,data,tree):
		try:		
			index = tree.element
			index2 = tree.decisions.index(data[index])
			if(type(tree.children[index2]) == str):
				return tree.children[index2]
			else:
				return self.testt(data,tree.children[index2])
		except ValueError:
            		return "No value"
		

	#Calc the entropy of the attributes
	def calc_info_gain(self, sample_data, r):

		if len(sample_data) == 0:
			print("Realización de la ejecución del programa con éxito")
		else:		

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
			
			
			information_gain_list =[]
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

			if(max(information_gain_list)!= 0):
				attributes_max = max(information_gain_list)
				index = information_gain_list.index(attributes_max)
				print ("Lista con todas las entropías de los valores de los atributos " , self.attrib_value_entropy_general_list)
				print("Indice del attributo con mayor ganancia :", index)
				print("Information gain of the attributes " + str(information_gain_list))
				tmp = self.calc_attrib_value_class(index,sample_data)
				print("Lista con los valores que poseen entropía igual cero y sus respectivas clases" , tmp)
				tmp2 = self.calc_no_attrib_value_class(index)
				print("Lista con los valores que poseen entropía diferente a cero y sus respectivas clases", tmp2)
				sample_data = self.calc_del_attrib_value_sd(tmp, index, sample_data)
				print("Nueva sample data ", sample_data)
				dt = Decision_tree(index)
				i = 0
				n = len(tmp)
				while(i<n):
					dt.decisions.append(tmp[i][0])
					dt.children.append(tmp[i][1])
					i += 1
				i = 0
				n = len(tmp2)
				while(i<n):
					dt.decisions.append(tmp2[i])
					dt.children.append(self.calc_info_gain(sample_data,self.r))
					i += 1
				return dt
			else:
				if(self.r == "r1"):
					return sample_data[0][len(sample_data[0])-2]
				else:
					return sample_data[0][len(sample_data[0])-1]

	


	def calc_attrib_value_class(self, index, sample_data):
		val = self.attrib_value_entropy_general_list[index] #list of the values with a class
		n = len(val)
		i = 0
		result_list = []
		while (i<n):
			if (val[i][1] == 0):
				tmp = val[i][0]
				for x in sample_data:
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

	def calc_del_attrib_value_sd(self, result_list,index, sample_data):
		i = 0
		n = len(result_list)
		drop = []
		while(i<n):
			j = 0
			m = len(sample_data)
			while(j < m):
				if (result_list[i][0] == sample_data[j][index]):
					drop.append(j)
				j += 1
			i += 1
		n = len(drop)
		i = 0
		drop = sorted(drop)
		print(drop)
		while(n > i):
			sample_data.pop(drop[n - 1])
			n -= 1
		n = len(sample_data)
		while(i < n):
			sample_data[i][index] = 0
			i += 1
		return sample_data
        
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
		#print("Cuenta del total de veces que aparece el valor del atributo " + str(count))
		return count

	#Calculate the probability of a value inside an attribute of the data
	def calc_value_prob(self, class_element,attrib_value,sample_data,class_list,class_type,attrib_value_position):
		prob_value = self.found_count_in_list(class_element,attrib_value,sample_data, class_list, class_type,attrib_value_position)/self.calc_attrib_value_found(attrib_value,sample_data,attrib_value_position)
		#print("Prob_value " + str(prob_value))
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
			#print ("IMPRIMIENDO EL RESULTADO DE LA PROBABILIDAD DE UN VALOR DE UN ATRIBUTO " + str(value_prob_list[j]))
			if (value_prob_list[j] == 0):
				entropy = entropy + 0
			else:
				entropy = entropy - (value_prob_list[j] * math.log(value_prob_list[j], base))		
		#print("Imprimiendo la entropía del valor " , attrib_value, entropy)
		#print("Imprimiendo la posicion del valor del atributo ", attrib_value_position)

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
	
	def convert_to_interval(self,data):
		i = 0
		n = len(data)
		while(i < n):
			if(data[i][2] < 50000):
				data[i][2] = "0 a 50000"
			elif(data[i][2] < 100000 and data[i][2] >= 50000):
				data[i][2] = "50000 a 100000"
			elif(data[i][2] < 150000 and data[i][2] >= 100000):
				data[i][2] = "100000 a 150000"
			elif(data[i][2] < 200000 and data[i][2] >= 150000):
				data[i][2] = "150000 a 200000"
			elif(data[i][2] > 200000):
				data[i][2] = "200000 a 250000"
			if(data[i][7] < 30):
				data[i][7] = "18 a 30"
			elif(data[i][7] < 50 and data[i][7] >= 30):
				data[i][7] = "30 a 50"
			elif(data[i][7] < 75 and data[i][7] >= 50):
				data[i][7] = "50 a 75"
			elif(data[i][7] < 150 and data[i][7] >= 75):
				data[i][7] = "75 a 100"
			data[i].pop(13)
			data[i].pop(9)
			data[i].pop(8)
			data[i].pop(4)
			data[i].pop(3)
			data[i].pop(1)
			i += 1
		return data


class Decision_tree:
	element = None
	children = None
	decisions = None

	def __init__(self, element):
		self.element = element #Index of the attribute in the data
		self.decisions = []		
		self.children = []
		

print("Iniciando el programa...")
#sample_data = [['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 55, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'],['HEREDIA', 'FLORES', 20037, 6.96, 2878.88, 'Urbana', 'Hombre', 41, 5763, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.61, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'],['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 48, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'],['SAN JOSE', 'PEREZ ZELEDON', 134534, 1905.51, 70.6, 'Rural', 'Mujer', 48, 38508, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.26, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'],['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 39, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'],['CARTAGO', 'EL GUARCO', 41793, 167.69, 249.23, 'Urbana', 'Hombre', 32, 10831, 3.83, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'],['CARTAGO', 'OREAMUNO', 45473, 201.31, 225.89, 'Urbana', 'Hombre', 57, 11232, 4.04, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.11, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'],['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 96, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA']]
sample_data = generar_muestra_pais(1000)
objeto = Decision_tree_model(sample_data[:500], "r21", 0)
i = 0
d = sample_data[500:]
n = len(d)
cor = 0
x = copy.deepcopy(d)
while(i<n):
	a = objeto.test(d[i])
	if(a==x[i][23]):
		cor += 1
	i += 1
print(cor)
#print(objeto.test(['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 55, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL']))
