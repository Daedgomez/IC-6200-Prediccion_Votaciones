import math
import pprint
import queue
#from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

pp = pprint.PrettyPrinter(indent=4)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.depth = None


    def pre_order(self):
        print(self.depth)
        print(self.value)
        
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

"""
def knn(k):
    kdtree = build_kdtree(data)
    pp.print(kdtree)
"""

def find_max(data, index):
    n = len(data)
    i = 0
    maxx = 0
    while(i < n):
        if (data[i][index] > maxx):
            maxx = data[i][index]
        i += 1
    return maxx
        

def distance(node1, node2):
    distance = 0
    n = len(node1)
    i = 0
    print(node1)
    print("")
    print(node2)
    while(i < n):
        if (isinstance(node1[i], str)):
            if(node1[i]==node2[i]):
                distance += 0
            else:
                distance += 1
        else:
            distance += (abs(node1[i]-node2[i])) / max([node1[i],max_data[i]])
        i+=1
    print("distnce")
    print(distance)
    print("")
    return distance

def closer_distance(pivot, node1, node2):
    if node1 is None:
        return node2

    if node2 is None:
        return node1

    d1 = distance(pivot, node1)
    d2 = distance(pivot, node2)

    if d1 < d2:
        return node1
    else:
        return node2

def kdtree_closest_point(root, point, depth=0):
    if root is None:
        return None
    kd = len(point)
    axis = depth % kd
    next_branch = None
    opposite_branch = None
    if point[axis] < root.value[axis]:
        next_branch = root.left_child
        opposite_branch = root.right_child
    else:
        next_branch = root.right_child
        opposite_branch = root.left_child


        
    best = closer_distance(point,kdtree_closest_point(next_branch,point,depth + 1),root.value)
    #if distance(point, best) > abs(point[axis] - root.value[axis]):
    best = closer_distance(point,kdtree_closest_point(opposite_branch,point,depth + 1),best)
    return best



def build_kdtree(points, depth=0):
    n = len(points)
    if n <= 0:
        return None
    kd = len(points[0])
    axis = depth % kd
    sorted_points = sorted(points, key=lambda point: point[axis])
    #print("depth")
    #print(depth)
    #print(sorted_points)
    medium = int(n/2)
    #print(n/2)
    node = BinaryTree(sorted_points[medium])
    node.depth = depth
    node.left_child = build_kdtree(sorted_points[:medium], depth + 1)
    node.right_child = build_kdtree(sorted_points[medium + 1:], depth + 1)
    return node

#data = generar_muestra_pais(7)

data = [['LIBERACION NACIONAL', 'SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Mujer', 51, 57355, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL'], ['INTEGRACION NACIONAL', 'ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Rural', 'Mujer', 52, 72031, 3.49, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA'], ['RESTAURACION NACIONAL', 'SAN JOSE', 'SANTA ANA', 49123, 61.42, 799.79, 'Urbana', 'Mujer', 22, 14235, 3.43, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.56, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL'], ['LIBERACION NACIONAL', 'CARTAGO', 'LA UNION', 99399, 44.83, 2217.24, 'Urbana', 'Hombre', 56, 26979, 3.67, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.51, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA'], ['RESTAURACION NACIONAL', 'HEREDIA', 'BARVA', 40660, 53.8, 755.76, 'Urbana', 'Hombre', 26, 11302, 3.59, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.13, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL'], ['INTEGRACION NACIONAL', 'PUNTARENAS', 'CORREDORES', 41831, 620.6, 67.4, 'Urbana', 'Hombre', 20, 11854, 3.52, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.25, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA'], ['ACCION CIUDADANA', 'SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 95, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA']]
print(data)
max_poblacion = find_max(data, 3)
max_superficie = find_max(data, 4)
max_densidad = find_max(data, 5)
max_edad = find_max(data, 8)
max_viviendas = find_max(data, 9)
max_ocupantes = find_max(data, 10)
max_escolaridad = find_max(data, 14)
max_data = [0,0,0,max_poblacion,max_superficie,max_densidad,0,0,max_edad,max_viviendas,max_ocupantes,0,0,0,max_escolaridad]
print(max_data)
print("NODO A PROBAR")
prueba = ['LIBERACION NACIONAL', 'GUANACASTE', 'SANTA CRUZ', 55104, 1312.27, 41.99, 'Rural', 'Hombre', 47, 16645, 3.31, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.72, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA']
print(prueba)
kdtree = build_kdtree(data)
print("")
#kdtree.pre_order()

print(kdtree_closest_point(kdtree, prueba, depth=0))
#print(kdtree.value)
#print(kdtree.right_child.value)
#print(kdtree.left_child.value)

