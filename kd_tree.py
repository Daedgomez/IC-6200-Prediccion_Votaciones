import queue
import collections
from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

class KNN:
    kdtree = None
    max_data = []    
    NN = []
    r = ""
    d = 0
    
    def __init__(self, data):
        max_poblacion = self.find_max(data, 2)
        max_superficie = self.find_max(data, 3)
        max_densidad = self.find_max(data, 4)
        max_edad = self.find_max(data, 7)
        max_viviendas = self.find_max(data, 8)
        max_ocupantes = self.find_max(data, 9)
        max_escolaridad = self.find_max(data, 13)
        self.max_data = [0,0,max_poblacion,max_superficie,max_densidad,0,0,max_edad,max_viviendas,max_ocupantes,0,0,0,max_escolaridad]
        self.kdtree = self.build_kdtree(data)

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

    def find_KNN(self,value,k,r_):
        self.NN = []
        self.r = r_
        if(self.r=="r21"):
            self.d = 1
        else:
            self.d = 0
        self.kdtree_closest_point(self.kdtree, value)
        self.NN
        return self.solve(k)
        
    def solve(self,k):
        s = sorted(self.NN, key=lambda x: x[1])
        index = 0
        if(self.r=="r1"):
            index = 22
        else:
            index = 23
        sk = s[:k+1]
        n = len(sk)
        i = 0
        result = []
        while(i < n):
            result.append(sk[i][0][index])
            i+=1
        cuenta1 = collections.Counter(result)
        return cuenta1.most_common(1)[0][0]
            
    def find_max(self,data, index):
        n = len(data)
        i = 0
        maxx = 0
        while(i < n):
            if (data[i][index] > maxx):
                maxx = data[i][index]
            i += 1
        return maxx    

    def distance(self,node1, node2):
        distance = 0
        n = len(node1)-2
        i = 0
        while(i < n+self.d):
            if (isinstance(node1[i], str)):
                if(node1[i]==node2[i]):
                    distance += 0
                else:
                    if(i==22):
                        distance += 10
                    else:
                        distance += 1
            else:
                distance += (abs(node1[i]-node2[i])) / max([node1[i],self.max_data[i]])
            i+=1
        return distance

    def closer_distance(self,pivot, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        d1 = self.distance(pivot, node1)
        d2 = self.distance(pivot, node2)
        if(not([node1,d1] in self.NN)):
            self.NN.append([node1,d1])
        if(not([node2,d2] in self.NN)):
            self.NN.append([node2,d2])
        if d1 < d2:     
            return node1
        else:
            return node2

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
      
        best = self.closer_distance(point,self.kdtree_closest_point(next_branch,point,depth + 1),root.value)
        best = self.closer_distance(point,self.kdtree_closest_point(opposite_branch,point,depth + 1),best)
        return best

    def build_kdtree(self,points, depth=0):
        n = len(points)
        if n <= 0:
            return None
        kd = len(points[0])
        axis = depth % kd
        sorted_points = sorted(points, key=lambda point: point[axis])
        medium = int(n/2)
        node = self.BinaryTree(sorted_points[medium])
        node.depth = depth
        node.left_child = self.build_kdtree(sorted_points[:medium], depth + 1)
        node.right_child = self.build_kdtree(sorted_points[medium + 1:], depth + 1)
        return node


data = generar_muestra_pais(2000)
knn = KNN(data[:1000])
dd = data[1000:]
n = len(dd)
print(n)
i=0
cor = 0
while(i<n):
    if (knn.find_KNN(dd[i], 5, "r21")==dd[i][23]):
        cor+=1
    print(cor)
    i+=1
#knn.find_KNN(prueba, 15, "r1")
#print("")
#print("")
#knn.find_KNN(prueba, 15, "r2")
#print("")
#print("")
#knn.find_KNN(prueba, 15, "r21")
