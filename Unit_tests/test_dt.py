## Archivo de pruebas unitarias para las funciones implementadas en el archivo _init_.py

from decisiontree import *

sample_data = [['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 55, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'],
        ['HEREDIA', 'FLORES', 20037, 6.96, 2878.88, 'Urbana', 'Hombre', 41, 5763, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.61, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'],
        ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 48, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'],
        ['SAN JOSE', 'PEREZ ZELEDON', 134534, 1905.51, 70.6, 'Rural', 'Mujer', 48, 38508, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.26, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'],
        ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 39, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'],
        ['CARTAGO', 'EL GUARCO', 41793, 167.69, 249.23, 'Urbana', 'Hombre', 32, 10831, 3.83, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'],
        ['CARTAGO', 'OREAMUNO', 45473, 201.31, 225.89, 'Urbana', 'Hombre', 57, 11232, 4.04, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.11, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'],
        ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 96, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA']]


def test_class_entropy():
	objeto = Decision_tree_model(sample_data, "r21", 0)
	assert objeto.class_entropy(22, sample_data) > 0
	
def test_calc_class_data():
	objeto = Decision_tree_model(sample_data, "r21", 0)
	assert (objeto.calc_class_data(22, sample_data)) != None




