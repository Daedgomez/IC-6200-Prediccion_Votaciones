from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia
import collections
class KNN:
    kdtree = None # Arbol binario donde se guardan los nodos
    max_data = [] # Calculo del maximo de en los atributos continuos para normalizarlos
    NN = [] # Vecinos mas cercanos
    r = "" # Tipo de prediccion
    d = 0 # Indice para medir la distancia 

    # Constructor
    def __init__(self, data):
        self.find_all_max(data)
        self.kdtree = self.build_kdtree(data)

    # Arbol binario
    class BinaryTree:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    # Encuentra los maximos en los datos continuos para normalizarlos
    def find_all_max(self, data):
        max_poblacion = self.find_max(data, 2)
        max_superficie = self.find_max(data, 3)
        max_densidad = self.find_max(data, 4)
        max_edad = self.find_max(data, 7)
        max_viviendas = self.find_max(data, 8)
        max_ocupantes = self.find_max(data, 9)
        max_escolaridad = self.find_max(data, 13)
        self.max_data = [0, 0, max_poblacion, max_superficie, max_densidad, 0, 0,
                         max_edad, max_viviendas, max_ocupantes, 0, 0, 0, max_escolaridad]

    # Prueba los datos
    def test(self, value, k, r_):
        self.NN = []
        self.r = r_
        if(self.r == "r21"):
            self.d = 1
        else:
            self.d = 0
        self.kdtree_closest_point(self.kdtree, value)
        return self.solve(k)

    # Toma en cuenta los vecinos cercanos (NN) para ver
    # cual es el resultado mas comun
    def solve(self, k):
        s = sorted(self.NN, key=lambda x: x[1])
        index = 0
        if(self.r == "r1"):
            index = 22
        else:
            index = 23
        sk = s[:k + 1]
        n = len(sk)
        i = 0
        result = []
        while(i < n):
            result.append(sk[i][0][index])
            i += 1
        cuenta1 = collections.Counter(result)
        return cuenta1.most_common(1)[0][0]

    # Encuentra el maximo de un atributo continuo
    def find_max(self,data, index):
        n = len(data)
        i = 0
        maxx = 0
        while(i < n):
            if (data[i][index] > maxx):
                maxx = data[i][index]
            i += 1
        return maxx    
 
    # Mide la distancia entre 2 nodos
    # |atributo1 - atributo2| si es continuo
    # 0 si atributo1 = atributo2 si es discreto
    # 1 si atributo1 != atributo2 si es discreto
    def distance(self, node1, node2):
        distance = 0
        n = len(node1) - 2
        i = 0
        while(i < n + self.d):
            if (isinstance(node1[i], str)):
                if(node1[i] == node2[i]):
                    distance += 0
                else:
                    if(i == 22):
                        distance += 10
                    else:
                        distance += 1
            else:
                distance += (abs(node1[i] - node2[i])) / max([node1[i], self.max_data[i]])
            i += 1
        return distance

    # Verifica cual nodo tiene menor distancia a un pivote
    def closer_distance(self,pivot, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        d1 = self.distance(pivot, node1)
        d2 = self.distance(pivot, node2)
        if(not([node1,d1] in self.NN)):
            self.NN.append([node1, d1])
        if(not([node2,d2] in self.NN)):
            self.NN.append([node2, d2])
        if d1 < d2:     
            return node1
        else:
            return node2

    # Recorre el kd-tree buscando los nodos con menor distancia
    def kdtree_closest_point(self,root, point, depth=0):
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
        best = self.closer_distance(point,
                self.kdtree_closest_point(next_branch, point, depth + 1), root.value)
        #best = self.closer_distance(point,
        #        self.kdtree_closest_point(opposite_branch,point, depth + 1), best)
        return best

    # Crea el arbol con los nodos de entrenamiento
    def build_kdtree(self,points, depth=0):
        n = len(points)
        if n <= 0:
            return None
        kd = len(points[0])
        axis = depth % kd
        sorted_points = sorted(points, key=lambda point: point[axis])
        medium = int(n/2)
        node = self.BinaryTree(sorted_points[medium])
        node.left_child = self.build_kdtree(sorted_points[:medium], depth + 1)
        node.right_child = self.build_kdtree(sorted_points[medium + 1:], depth + 1)
        return node


def test_f1():
    knn = KNN(generar_muestra_pais(100))
    assert type(knn) is KNN

def test_f2():
    knn = KNN(generar_muestra_pais(100))
    a = generar_muestra_pais(2)
    assert type(knn.test(a[0],5,"r1")) is str

def test_f3():
    knn = KNN(generar_muestra_pais(100))
    knn.build_kdtree(generar_muestra_pais(100))
    assert type(knn.build_kdtree(generar_muestra_pais(100))) is knn.BinaryTree
